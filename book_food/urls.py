from django.urls import path
from . import views
from .views import cancel_reservation

urlpatterns = [
    path('', views.ReservationList.as_view(), name='home'),
    path('make_reservation/', views.make_reservation, name="make_reservation" ),
    path('make_reservation/confirmation/', views.reservation_success, name="reservation_success"),
    path('bookings/', views.BookingsListView.as_view(), name='bookings'),
    path('cancel_reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
]