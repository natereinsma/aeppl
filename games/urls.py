from django.urls import path

from . import views

urlpatterns = [
    path('game_board', views.game_board, name='game_board'),
]