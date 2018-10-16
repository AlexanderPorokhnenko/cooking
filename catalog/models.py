from django.db import models
from django.urls import reverse
import uuid, datetime

class Kitchen(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    kitchen_vars = (
        ('japan','Японская'),
        ('china','Китайская'),
        ('italia', 'Итальянская'),
        ('russian', 'Русская'),
        ('ukrainian', 'Украинская'),
        ('french', 'Французская'),
        ('usa', 'Американская'),
        ('european', 'Европейская'),
        ('asian', 'Азиатская'),
        ('african', 'Африканская'),
    )
    kitchen = models.CharField(max_length=100, choices=kitchen_vars)

    def __str__(self):
        return self.kitchen

class Kind(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    kind_vars = (
        ('first', 'Первые блюда'),
        ('second', 'Вторые блюда'),
        ('snack', 'Закуски'),
        ('dessert', 'Десерты'),
        ('salat', 'Салаты'),
        ('drink', 'Напитки')
    )

    kind = models.CharField(max_length=100, choices=kind_vars, unique=True)

    def __str__(self):
        return self.kind

class Recept(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the title of the article')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID of recept', editable=False, unique=True)
    text = models.TextField(help_text='Enter text of article')
    photos = models.ImageField(help_text='Attach images', null=True, upload_to='static/img/blog-img')
    kitchen = models.ManyToManyField(Kitchen, help_text='Select a kitchen for this recept')
    ingridients = models.TextField(help_text='List and quantity of ingridients', default='')
    kind = models.ForeignKey('Kind', on_delete=models.SET_NULL, null=True)
    current_date = models.DateField(default=datetime.date.today)
    stars_choice = ((1,1), (2,2), (3,3), (4,4), (5,5))
    stars = models.IntegerField(choices=stars_choice, default=3)

    def __str__(self):
        return self.title

    def slpit_text(self):
        return str(self.text).split(';')

    def slpit_ingridients(self):
        return str(self.ingridients).split(';')

    def get_absolute_url(self):
        return reverse('receipt-detail', args=[str(self.id)])

class Subscriptions(models.Model):
    email = models.EmailField(max_length=55)


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    current_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.subject) +" " + str(self.email) + " " + str(self.current_date)

class Article(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    pictures = models.ImageField(null=False, upload_to='static/img/articles')
    text = models.TextField(help_text='Enter text of article')
    current_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])





