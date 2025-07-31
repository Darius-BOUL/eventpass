from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from tickets.models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def simulate_payment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if request.method == 'POST':
        Payment.objects.create(
            ticket=ticket,
            amount=ticket.total_price(),
            status='success'
        )
        ticket.is_paid = True
        ticket.save()
        return redirect('payment_success')

    return render(request, 'payments/simulate_payment.html', {
        'ticket': ticket
    })

def payment_success(request):
    return render(request, 'payments/payment_success.html')
