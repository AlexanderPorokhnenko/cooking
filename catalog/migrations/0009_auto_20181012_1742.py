# Generated by Django 2.1.2 on 2018-10-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20181012_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kind',
            name='kind',
            field=models.CharField(choices=[('first', 'Первые блюда'), ('second', 'Вторые блюда'), ('snack', 'Закуски'), ('dessert', 'Десерты'), ('salat', 'Салаты'), ('drink', 'Напитки')], max_length=100, unique=True),
        ),
    ]
