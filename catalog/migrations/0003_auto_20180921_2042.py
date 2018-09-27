# Generated by Django 2.1.1 on 2018-09-21 17:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180919_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.CharField(choices=[('japan', 'Japanese'), ('china', 'China'), ('italia', 'Italiano'), ('europe', 'European'), ('unknown', 'Unknown')], default='unknown', help_text='Specify country for recept', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='recept',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID of recept', primary_key=True, serialize=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='recept',
            name='kitchen',
        ),
        migrations.AddField(
            model_name='recept',
            name='kitchen',
            field=models.ManyToManyField(to='catalog.Kitchen'),
        ),
    ]
