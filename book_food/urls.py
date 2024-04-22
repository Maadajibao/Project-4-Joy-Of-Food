from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationList.as_view(), name='home'),
    path('make_reservation/', views.make_reservation, name="make_reservation" ),
    path('make_reservation/confirmation/', views.reservation_success, name="reservation_success"),
    path('bookings/', views.BookingsListView.as_view(), name='bookings'),
]