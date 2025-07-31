from django.urls import path
from . import views

urlpatterns = [
    path('reserve/<int:event_id>/', views.reserve_ticket, name='reserve_ticket'),
]
