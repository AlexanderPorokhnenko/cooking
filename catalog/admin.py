from django.contrib import admin
from .models import Recept, Kitchen, Kind, Subscriptions

admin.site.register(Recept)
admin.site.register(Kind)
admin.site.register(Kitchen)
admin.site.register(Subscriptions)