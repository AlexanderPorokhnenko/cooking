# Generated by Django 2.1.2 on 2018-10-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20181017_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='text',
            field=models.TextField(default='', help_text='Enter text of recept'),
        ),
    ]