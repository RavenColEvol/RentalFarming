from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from user.models import User


class Implementation(models.Model):
    implement = models.CharField(max_length=50, )

    def __str__(self):
        return self.implement


class MyImplementation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    implement = models.ManyToManyField(Implementation)

    def __str__(self):
        return self.user.phone_number


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

    drive = models.IntegerField(_('drive'))
    hp = models.IntegerField(_('hp'))
    rent_per_hour = models.IntegerField(_('rent per hour'))
    brand_name = models.CharField(_('brand'), max_length=30, choices=TRACTOR_COMPANY_CHOICE, default='1')
    model_name = models.CharField(_('model'), max_length=30)
    note = models.TextField(_('note'), blank=True)

    def __str__(self):
        return str(self.brand_name) + ' - ' + str(self.model_name)

    def get_absolute_url(self):
        return reverse('tractor:detail', kwargs={'pk': self.pk})


def create_implementation(sender, instance, **kwargs):
    if kwargs['created'] and sender.is_renter:
        MyImplementation.objects.create(user=instance)


post_save.connect(receiver=create_implementation, sender=User)
