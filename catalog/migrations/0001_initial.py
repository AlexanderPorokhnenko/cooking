# Generated by Django 2.1.1 on 2018-09-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the article', max_length=200)),
                ('text', models.TextField(help_text='Enter text of article')),
                ('kitchen', models.CharField(help_text='What country?', max_length=50)),
                ('kind', models.CharField(help_text='What kind of recept?', max_length=50)),
            ],
        ),
    ]
