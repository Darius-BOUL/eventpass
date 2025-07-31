from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'amount', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('ticket__user__username', 'ticket__event__title')
