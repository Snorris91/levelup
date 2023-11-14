from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    number_of_players = models.PositiveBigIntegerField()
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="game_type")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_created")
