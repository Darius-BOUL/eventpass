from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from tickets.models import Ticket

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def create_event(request):
    if not request.user.is_organizer:
        return redirect('event_list')
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form})


@login_required
def organizer_dashboard(request):
    if not request.user.is_organizer:
        return redirect('event_list')

    events = Event.objects.filter(organizer=request.user)
    dashboard_data = []

    for event in events:
        tickets = Ticket.objects.filter(event=event, is_paid=True)
        total_sold = sum(ticket.quantity for ticket in tickets)
        total_revenue = total_sold * event.ticket_price

        dashboard_data.append({
            'event': event,
            'total_sold': total_sold,
            'total_revenue': total_revenue,
        })

    return render(request, 'events/organizer_dashboard.html', {
        'dashboard_data': dashboard_data
    })

