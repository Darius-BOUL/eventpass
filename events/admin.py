from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date', 'location', 'ticket_price', 'total_tickets')
    list_filter = ('date', 'organizer')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date',)
