# Generated by Django 5.0.6 on 2024-06-28 18:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userprofile_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='creationDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]