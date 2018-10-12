from django.contrib import admin
from .models import Recept, Article, Message, Kind

admin.site.register(Recept)
admin.site.register(Article)
admin.site.register(Message)
admin.site.register(Kind)