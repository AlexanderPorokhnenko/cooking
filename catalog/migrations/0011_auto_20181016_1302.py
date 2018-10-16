# Generated by Django 2.1.2 on 2018-10-16 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20181016_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='kind_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Kind'),
        ),
        migrations.AddField(
            model_name='recept',
            name='kind_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Kind'),
        ),
        migrations.AddField(
            model_name='recept',
            name='kind_uk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Kind'),
        ),
    ]