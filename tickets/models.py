from django.db import models
from django.conf import settings
from events.models import Event

#import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def generate_qr_code(self):
        data = f"Ticket ID: {self.id}\nEvent: {self.event.title}\nUser: {self.user.username}"
        #qr = qrcode.make(data)
        buffer = BytesIO()
        #qr.save(buffer, format='PNG')
        file_name = f"ticket-{self.id}.png"
        self.qr_code.save(file_name, File(buffer), save=False)

    def total_price(self) -> int:
        return self.quantity * self.event.ticket_price

    def __str__(self):
        return f"{self.user.username} - {self.event.title} x {self.quantity}"
