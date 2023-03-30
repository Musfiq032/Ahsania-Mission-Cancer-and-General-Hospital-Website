from django.conf.urls.static import static
from django.conf import settings
from Services.views import *
from django.urls import path

app_name = 'Services'
urlpatterns = [

                path('room-rent/', room_rent_view, name='room-rent'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
