from django.db import models
from django.conf import settings

class Event(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_tickets = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
