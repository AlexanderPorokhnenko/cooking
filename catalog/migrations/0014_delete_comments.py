# Generated by Django 2.1.2 on 2018-10-16 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_comments_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]