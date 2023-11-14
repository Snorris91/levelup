from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_by")
    attendees = models.ManyToManyField(
        User,
        through='EventGame',
        related_name="Events"
    )
