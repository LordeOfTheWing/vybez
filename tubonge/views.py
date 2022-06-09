from django.shortcuts import render
from .models import Room
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn django'},
    {'id': 2, 'name': 'Lets learn django'},
    {'id': 3, 'name': 'Lets learn python'},
    {'id': 4, 'name': 'Lets learn react'},
    {'id': 5, 'name': 'Lets learn typescript'},
    {'id': 6, 'name': 'Lets learn redux'},
    {'id': 7, 'name': 'Lets learn jwt'},
    {'id': 7, 'name': 'Lets learn jwt'},
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'tubonge/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}
    return render(request, 'tubonge/room.html', context)
