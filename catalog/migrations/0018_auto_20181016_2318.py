# Generated by Django 2.1.2 on 2018-10-16 20:18

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20181016_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelist',
            name='image1',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='imagelist',
            name='image2',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='recept',
            name='ph',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.ImageList'),
        ),
        migrations.AlterField(
            model_name='recept',
            name='photos',
            field=models.ImageField(help_text='Attach image 1920x735', max_length=250, null=True, upload_to=catalog.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='recept',
            name='preview_photo',
            field=models.ImageField(help_text='Attach image for preview 110x110', max_length=200, null=True, upload_to=catalog.models.upload_path_handler),
        ),
    ]
