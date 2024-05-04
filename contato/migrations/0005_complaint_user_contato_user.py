# Generated by Django 5.0.4 on 2024-05-02 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0004_remove_complaint_email_remove_complaint_nome_and_more'),
        ('store', '0006_delete_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.profile'),
        ),
        migrations.AddField(
            model_name='contato',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.profile'),
        ),
    ]