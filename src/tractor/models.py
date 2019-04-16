from django.db import models
from django.urls import reverse

from user.models import User  # This is no error. Don't worry


class Implementation(models.Model):
    implement = models.CharField(max_length=50,)

    def __str__(self):
        return self.implement


class MyImplementation(models.Model):
    implement = models.ManyToManyField(Implementation)


class Tractor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True)

    TRACTOR_COMPANY_CHOICE = (
        ('John Deere', 'John Deere'),
        ('Tafe', 'Tafe'),
        ('Escorts', 'Escorts'),
        ('Swaraj', 'Swaraj'),
        ('Mahindra', 'Mahindra'),
        ('Sonalika', 'Sonalika'),
        ('Trakstar', 'Trakstar'),
        ('Kubota', 'Kubota'),
    )

    RENT_CHOICE = (
        ('ACRE', 'PER ACRE'),
        ('HOUR', 'PER HOUR')
    )
    Drive = models.IntegerField()
    Hp = models.IntegerField()
    RentPerHour = models.IntegerField()
    brand_name = models.CharField(max_length=30, choices=TRACTOR_COMPANY_CHOICE, default='1')
    model_name = models.CharField(max_length=30)
    rent_choice = models.CharField(max_length=10, choices=RENT_CHOICE, default='HOUR')
    working_radius = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.brand_name) + ' - ' + str(self.model_name)

    # def get_absolute_url(self):
    #     return reverse('tractor:detail', kwargs={'pk'})
