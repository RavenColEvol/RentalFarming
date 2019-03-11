from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class TractorInfo(models.Model):
    Owner_Name = models.CharField(max_length=150)
    Tractor_Name = models.CharField(max_length=150,default='Unkown')
    City = models.CharField(max_length=50)
    Drive = models.IntegerField()
    Hp = models.IntegerField()
    RentPerHour = models.IntegerField()
    Image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.Owner_Name + self.City


class OwnerInfo(models.Model):
    STATE_CHOICE = (
        ('MH','Maharashtra'),
    )
    CITY_CHOICE = (
        ('TH','Thane'),
    )
    username = models.CharField(max_length=150)
    email = models.EmailField()
    number = PhoneNumberField()
    pincode = models.IntegerField()
    state = models.CharField(
        max_length=2,
        choices = STATE_CHOICE,
        default='MH'
        )
    city = models.CharField(
        max_length=2,
        choices = CITY_CHOICE,
        default='TH'
    )
    address = models.TextField()

    def __str__(self):
        return self.email