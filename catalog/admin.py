from django.contrib import admin
from .models import Recept, Article, Message, Kind, Kitchen, ImageList

admin.site.register(Recept)
admin.site.register(ImageList)
admin.site.register(Article)
admin.site.register(Message)
admin.site.register(Kind)
admin.site.register(Kitchen)
