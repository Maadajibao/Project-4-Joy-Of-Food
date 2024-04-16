from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    num_tables = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.party_size} guests on {self.date} at {self.time}"
