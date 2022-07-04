from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game_board(request):
    return HttpResponse('Hello')