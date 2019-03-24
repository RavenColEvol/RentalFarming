# Generated by Django 2.1.7 on 2019-03-24 13:46

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(choices=[('MH', 'Maharashtra')], default='MH', max_length=2)),
                ('city', models.CharField(
                    choices=[('TH', 'Thane'), ('NA', 'Nashik'), ('DH', 'Dhule'), ('AK', 'Akola'), ('CH', 'Chandrapu'),
                             ('LA', 'Latur'), ('PA', 'Parbhani'), ('SO', 'Solapur'), ('YA', 'Yavatmal')], default='TH',
                    max_length=2)),
                ('address', models.TextField()),
                ('Drive', models.IntegerField()),
                ('Hp', models.IntegerField()),
                ('RentPerHour', models.IntegerField()),
                ('Image', models.ImageField(null=True, upload_to='media/')),
                ('brand_name', models.CharField(
                    choices=[('1', 'John Deere'), ('2', 'Tafe'), ('3', 'Escorts'), ('4', 'Swaraj'), ('5', 'Mahindra'),
                             ('6', 'Sonalika'), ('7', 'Trakstar'), ('8', 'Kubota')], default='1', max_length=30)),
                ('model_name', models.CharField(max_length=30)),
                ('implement', models.CharField(
                    choices=[('1', 'Baler'), ('2', 'Combine Harvester'), ('3', 'Cultivator'), ('4', 'Disc Harrow'),
                             ('5', 'Disc Plough'), ('6', 'Hole Digger'), ('7', 'Hydraulic reversible plough '),
                             ('8', 'Mould Board Plough'), ('9', 'Potato Harvester'), ('10', 'Power Harrow'),
                             ('11', 'Power Tiller'), ('12', 'Rice Transplanter'), ('13', 'Rotary Tiller'),
                             ('14', 'Rotavator'), ('15', 'Row Potato Planter'), ('16', 'Seed Drill'), ('17', 'Sprayer'),
                             ('18', 'Straw Reaper'), ('19', 'Sugarcane Harvester'), ('20', 'Thresher')], default='1',
                    max_length=2)),
                ('rent_choice',
                 models.CharField(choices=[('ACER', 'PER ACER'), ('HOUR', 'PER HOUR')], default='HOUR', max_length=10)),
                ('working_radius', models.IntegerField()),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
