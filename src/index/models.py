from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    username = models.CharField(max_length=150)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.username


class RentForm(models.Model):
    STATE_CHOICE = (
        ('MH', 'Maharashtra'),
    )
    CITY_CHOICE = (
        ('Thane', 'Thane'),
        ('Nashik', 'Nashik'),
        ('Dhule', 'Dhule'),
        ('Akola', 'Akola'),
        ('Chandrapu', 'Chandrapu'),
        ('Latur', 'Latur'),
        ('Parbhani', 'Parbhani'),
        ('Solapur', 'Solapur'),
        ('Yavatmal', 'Yavatmal'),
    )
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField()
    number = PhoneNumberField()
    pincode = models.IntegerField()
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICE,
        default='MH'
    )
    city = models.CharField(
        max_length=30,
        choices=CITY_CHOICE,
        default='TH'
    )
    address = models.TextField()

    TRACTOR_CHOICE = (
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
    brand_name = models.CharField(max_length=30, choices=TRACTOR_CHOICE, default='1')
    model_name = models.CharField(max_length=30)
    implement = models.CharField(max_length=2, choices=IMPLEMENT_CHOICE, default='1')
    rent_choice = models.CharField(max_length=10, choices=RENT_CHOICE, default='HOUR')
    working_radius = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.username) + ' ' + str(self.city)
