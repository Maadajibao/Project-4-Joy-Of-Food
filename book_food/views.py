from django.shortcuts import render
from django.views import generic
from .models import Reservation

# Create your views here.

class ReservationList(generic.ListView):
    model = Reservation
    template_name = "index.html"
    paginate_by = 6
