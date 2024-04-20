from django.shortcuts import render
from django.views import generic
from .models import Reservation

# Create your views here.

class ReservationList(generic.ListView):
    model = Reservation
    template_name = "index.html"
    paginate_by = 6


def make_reservation(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        party_size = request.POST['party_size']
        num_tables = request.POST['num_tables']

        # Create a new reservation and save it to database

        reservation = Reservation(date=date, time=time, party_size=party_size, num_tables=num_tables)
        reservation.save()