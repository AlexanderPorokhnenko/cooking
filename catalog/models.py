from django.db import models
from django.urls import reverse
import uuid, datetime
from django.conf import settings

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


def upload_path_handler(instance, filename):
    return settings.MEDIA_URL + "{title}/{file}".format(title=instance.title, file=filename)


class ImageList(models.Model):

    title = models.CharField(max_length=200, help_text='Enter the title of the article', null=True)
    title_image1 = models.ImageField(null=True, upload_to=upload_path_handler, help_text='Title image 1920x735')
    title_image2 = models.ImageField(null=True, upload_to=upload_path_handler, help_text='Title image 1920x735')
    title_image3 = models.ImageField(null=True, upload_to=upload_path_handler, help_text='Title image 1920x735', blank=True)
    preview_image = models.ImageField(null=True, upload_to=upload_path_handler, help_text='Preview image 110x110')
    slider_image = models.ImageField(null=True, upload_to=upload_path_handler, help_text='Slider image 1920x1280', blank=True)

    def __iter__(self):
        return iter([self.title_image1, self.title_image2, self.title_image3, self.preview_image, self.slider_image])

    def __str__(self):
        return str(self.title)


class Recept(models.Model):

    title = models.CharField(max_length=200, help_text='Enter the title of the article')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID of recept', editable=False, unique=True)
    text = models.TextField(help_text='Enter text of recept', default='')
    kitchen = models.ManyToManyField(Kitchen, help_text='Select a kitchen for this recept')
    ingridients = models.TextField(help_text='List and quantity of ingridients', default='')
    kind = models.ForeignKey('Kind', on_delete=models.SET_NULL, null=True)
    current_date = models.DateField(default=datetime.date.today)
    stars_choice = ((1,1), (2,2), (3,3), (4,4), (5,5))
    stars = models.IntegerField(choices=stars_choice, default=3)
    ph = models.ForeignKey(ImageList, on_delete=models.SET_NULL, null=True, max_length=200)
    tags = models.CharField(default='', max_length=300, help_text='Tags separated bt comma')
    slider = models.BooleanField(help_text='Is field for slider?', default=False)
    cook_time = models.CharField(max_length=20, help_text='Enter 3 digits separated by "$". Prepare time, cooking time, yields', default='')

    def __str__(self):
        return str(self.title)

    def split_tags(self):
        return [x.strip() for x in str(self.tags).split(',') if x]

    def split_text(self):
        return [x.strip() for x in str(self.text).split(';') if x]

    def slpit_ingridients(self):
        return [x.strip() for x in str(self.ingridients).split(';') if x]

    def slpit_cook_time(self):
        return [x.strip() for x in str(self.cook_time).split(';') if x]

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
        return str(self.subject) + " " + str(self.email) + " " + str(self.current_date)


class Article(models.Model):

    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    pictures = models.ImageField(null=False, upload_to='static/img/articles', help_text='Image for article 900x300')
    text = models.TextField(help_text='Enter text of article')
    current_date = models.DateField(default=datetime.date.today)
    tags = models.CharField(max_length=300, default='', help_text='Tags separated by comma')

    def split_tags(self):
        return [x.strip() for x in str(self.tags).split(',') if x]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])





