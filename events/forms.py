from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Date et heure de l'événement"
    )

    class Meta:
        model = Event
        fields = ['title', 'description','image', 'location', 'date', 'ticket_price', 'total_tickets']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

