# Generated by Django 2.1.2 on 2018-10-10 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181009_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='current_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
