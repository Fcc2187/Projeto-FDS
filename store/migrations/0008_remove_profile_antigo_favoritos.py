# Generated by Django 5.0.6 on 2024-05-13 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_profile_antigo_favoritos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='antigo_favoritos',
        ),
    ]