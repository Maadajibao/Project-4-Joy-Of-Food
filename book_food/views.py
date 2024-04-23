from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

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

        # Check for double bookings
        existing_reservations = Reservation.objects.filter(date=date, time=time)
        if existing_reservations.exists():
            messages.error(request, "Sorry, there is already a reservation for this date and time.")
            return render(request, 'messages.html')

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



class BookingsListView(generic.ListView):
    model = Reservation
    template_name = 'bookings.html'
    context_object_name = 'bookings'

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        #Perform cancellation
        reservation.delete()
        messages.success(request, "Reservation cancelled successfully.")
        return render(request,'cancel_reservation.html',) 
    return render(request, 'cancel_reservation.html', {'reservation': reservation})
    
    