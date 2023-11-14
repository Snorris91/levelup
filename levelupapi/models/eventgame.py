from django.db import models
from django.contrib.auth.models import User

class EventGame(models.Model):
    event = models.ForeignKey("Events", on_delete=models.CASCADE, related_name="event_created")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendees")
