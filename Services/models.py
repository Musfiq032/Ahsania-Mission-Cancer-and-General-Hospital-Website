from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class RoomRent(models.Model):
    Room_Type = models.CharField(max_length=100, null=True, blank=True)
    Room_Rate = models.IntegerField(default='0', null=True, blank=True)
    discounted_price = models.IntegerField(default=0, null=True, blank=True)
    Room_Image = models.ImageField(upload_to='Room', null=True, blank=True)

    def __str__(self):
        return self.Room_Type


class PackageType(models.Model):
    name = models.CharField(max_length=100, blank=False)
    package_price_optional = models.CharField(max_length=100, blank=True, null=True, default="0")

    def __str__(self):
        return self.name


class Package(models.Model):
    package_type = models.ManyToManyField(PackageType)
    package_name = models.CharField(max_length=100, null=False, blank=False)
    package_price = models.IntegerField(default=0, blank=False, null=False)
    package_details = RichTextField(blank=True, default="(Optional)")

    def __str__(self):
        return self.package_name


class PopupBanner(models.Model):
    popup_banner_image = models.ImageField(upload_to='PopUp_Banners')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

