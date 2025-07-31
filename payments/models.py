from django.db import models
from tickets.models import Ticket
from django.utils import timezone
1

class Payment(models.Model):
    ticket = models.OneToOneField('tickets.Ticket', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    

     

