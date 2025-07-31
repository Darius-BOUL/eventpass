from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from .models import Payment


@login_required
def simulate_payment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    # 🔐 Empêche de recréer un paiement s'il existe déjà
    if Payment.objects.filter(ticket=ticket).exists():
        return redirect('payment_success', ticket_id=ticket.id)

    if request.method == 'POST':
        # marquer le ticket comme payé
        ticket.is_paid = True
        ticket.generate_qr_code()
        ticket.save()

        # créer un paiement
        Payment.objects.create(
            ticket=ticket,
            amount=ticket.total_price()
        )

        return redirect('payment_success', ticket_id=ticket.id)

    return render(request, 'payments/simulate_payment.html', {'ticket': ticket})


@login_required
def payment_success(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'payments/payment_success.html', {'ticket': ticket})

