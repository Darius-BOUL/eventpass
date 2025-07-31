from django.urls import path
from . import views

urlpatterns = [
    path('simulate/<int:ticket_id>/', views.simulate_payment, name='simulate_payment'),
    path('success/', views.payment_success, name='payment_success'),
]
