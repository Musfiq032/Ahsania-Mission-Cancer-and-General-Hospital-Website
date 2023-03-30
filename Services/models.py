from django.db import models

# Create your models here.

class RoomRent(models.Model):
    Room_Type= models.CharField(max_length=100, null= True, blank=True)
    Room_Rate= models.IntegerField(default='0', null= True, blank=True)
    Room_Image= models.ImageField(upload_to='Room', null= True, blank=True)
