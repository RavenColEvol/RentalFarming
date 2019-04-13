from django.db import models

from user.models import User  # This is no error. Don't worry


class Tractor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    IMPLEMENT_CHOICE = (
        ('1', 'Baler'),
        ('2', 'Combine Harvester'),
        ('3', 'Cultivator'),
        ('4', 'Disc Harrow'),
        ('5', 'Disc Plough'),
        ('6', 'Hole Digger'),
        ('7', 'Hydraulic reversible plough '),
        ('8', 'Mould Board Plough'),
        ('9', 'Potato Harvester'),
        ('10', 'Power Harrow'),
        ('11', 'Power Tiller'),
        ('12', 'Rice Transplanter'),
        ('13', 'Rotary Tiller'),
        ('14', 'Rotavator'),
        ('15', 'Row Potato Planter'),
        ('16', 'Seed Drill'),
        ('17', 'Sprayer'),
        ('18', 'Straw Reaper'),
        ('19', 'Sugarcane Harvester'),
        ('20', 'Thresher'),
    )

    RENT_CHOICE = (
        ('ACRE', 'PER ACRE'),
        ('HOUR', 'PER HOUR')
    )
    Drive = models.IntegerField()
    Hp = models.IntegerField()
    RentPerHour = models.IntegerField()
    Image = models.ImageField(upload_to="media/", null=True)
    brand_name = models.CharField(max_length=30, choices=TRACTOR_COMPANY_CHOICE, default='1')
    model_name = models.CharField(max_length=30)
    implement = models.CharField(max_length=2, choices=IMPLEMENT_CHOICE, default='1')
    rent_choice = models.CharField(max_length=10, choices=RENT_CHOICE, default='HOUR')
    working_radius = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.brand_name) + ' - ' + str(self.model_name)
