from django.shortcuts import render, redirect
from django.views import generic
from .models import Reservation
from django.contrib.auth.decorators import login_required


# Create your views here.

class ReservationList(generic.ListView):
    model = Reservation
    template_name = "index.html"
    paginate_by = 6



@login_required
def make_reservation(request):
    if request.method == 'POST':
        # Get the logged-in user
        user = request.user

        # Retrieve form data
        date = request.POST['date']
        time = request.POST['time']
        party_size = request.POST['party_size']
        num_tables = request.POST['num_tables']

        # Create a new reservation and save it to database
        reservation = Reservation.objects.create(
            user=user,
            date=date, 
            time=time, 
            party_size=party_size, 
            num_tables=num_tables)
        reservation.save()

       
        # Redirect to the reservation success page
        return redirect('reservation_success')
    
    return render(request, 'base.html')

def reservation_success(request):

    return render(request, 'reservation_success.html')
    
    