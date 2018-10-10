from django.forms import ModelForm
from .models import Subscriptions

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriptions
        fields = ['email']