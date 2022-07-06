from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Enter_Game(models.Model):
    player_one = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name='player_one_game')
    player_two = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name='player_two_game')
    num_games = models.SmallIntegerField(default = 3)

    game_one_p_1 = models.SmallIntegerField(default = 0)
    game_one_p_2 = models.SmallIntegerField(default = 0)
    game_two_p_1 = models.SmallIntegerField(default = 0)
    game_two_p_2 = models.SmallIntegerField(default = 0)
    game_three_p_1 = models.SmallIntegerField(default = 0)
    game_three_p_2 = models.SmallIntegerField(default = 0)
    game_four_p_1 = models.SmallIntegerField(default = 0)
    game_four_p_2 = models.SmallIntegerField(default = 0)
    game_five_p_1 = models.SmallIntegerField(default = 0)
    game_five_p_2 = models.SmallIntegerField(default = 0)
    game_six_p_1 = models.SmallIntegerField(default = 0)
    game_six_p_2 = models.SmallIntegerField(default = 0)
    game_seven_p_1 = models.SmallIntegerField(default = 0)
    game_seven_p_2 = models.SmallIntegerField(default = 0)

    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='winner_game')

    created = models.DateTimeField(auto_now_add=True)

class Validate_Game(models.Model):
    game_id = models.ForeignKey(Enter_Game, on_delete=models.CASCADE)
    validated = models.CharField(max_length=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
