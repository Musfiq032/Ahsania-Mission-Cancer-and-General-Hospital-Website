from django.shortcuts import render

from Services.models import *


# Create your views here.

def room_rent_view(request):
    room_info = RoomRent.objects.all()

    context = {
        'room_info': room_info,


    }
    return render(request, 'Services/room_rent.html', context)
