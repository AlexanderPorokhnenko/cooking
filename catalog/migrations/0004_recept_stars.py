# Generated by Django 2.1.2 on 2018-10-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_recept_current_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
    ]
