from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'quantity', 'is_paid', 'purchased_at')
    list_filter = ('is_paid', 'event')
    search_fields = ('user__username', 'event__title')
