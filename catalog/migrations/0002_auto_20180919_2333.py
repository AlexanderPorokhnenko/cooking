# Generated by Django 2.1.1 on 2018-09-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='photos',
            field=models.ImageField(help_text='Attach images', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recept',
            name='kitchen',
            field=models.CharField(choices=[('j', 'Japanese'), ('ch', 'China')], help_text='What country?', max_length=50),
        ),
    ]
