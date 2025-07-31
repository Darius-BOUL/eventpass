from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['quantity']
        labels = {
            'quantity': 'Nombre de billets',
        }
