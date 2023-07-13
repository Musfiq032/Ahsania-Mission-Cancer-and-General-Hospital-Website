from django.shortcuts import render

from Services.models import *


# Create your views here.

def room_rent_view(request):
    room_info = RoomRent.objects.all()

    context = {
        'room_info': room_info,

    }
    return render(request, 'Services/room_rent.html', context)


def package_view(request):
    # first_package_type = PackageType.objects.first()
    package_type = PackageType.objects.all()
    filtered_type= PackageType.objects.all()[1:]
    # package = Package.objects.all()
    gayne_dep_package= Package.objects.filter(package_type__in="0")

    context = {
        'filtered_type': filtered_type,
        'package_type': package_type,
        'gayne_dep_package': gayne_dep_package

    }
    return render(request, 'Services/package.html', context)
