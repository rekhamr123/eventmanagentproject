from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('event_detail/<int:id>', views.eve_detail, name='event_detail'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
]

