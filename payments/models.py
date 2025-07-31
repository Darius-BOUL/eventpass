from django.db import models
from tickets.models import Ticket

class Payment(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)
