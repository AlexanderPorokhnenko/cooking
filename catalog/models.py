from django.db import models
from django.urls import reverse
import uuid

class Kitchen(models.Model):
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
    kind_vars = (
        ('first', 'Первое блюдо'),
        ('second', 'Второе блюдо'),
        ('snack', 'Закуски'),
        ('dessert', 'Десерт'),
        ('salat', 'Салат'),
        ('drink', 'Напиток')
    )

    kind = models.CharField(max_length=100, choices=kind_vars)

    def __str__(self):
        return self.kind

class Recept(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the title of the article')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID of recept', editable=False, unique=True)
    text = models.TextField(help_text='Enter text of article')
    photos = models.ImageField(help_text='Attach images', null=True)
    kitchen = models.ManyToManyField(Kitchen, help_text='Select a kitchen for this recept')
    kind = models.ForeignKey('Kind', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('recept_detail', args=[str(self.id)])


