# Generated by Django 5.0.4 on 2024-06-26 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
