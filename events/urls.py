from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create_event'),
    path('dashboard/', views.organizer_dashboard, name='organizer_dashboard'),

]
