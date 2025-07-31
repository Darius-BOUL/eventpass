from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from events.models import Event

@login_required
def reserve_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.event = event
            ticket.save()
            ticket.generate_qr_code()
            ticket.save()
            return redirect('simulate_payment', ticket_id=ticket.id)
    else:
        form = TicketForm()

    return render(request, 'tickets/reserve_ticket.html', {
        'form': form,
        'event': event
    })

