from django.forms import ModelForm
from .models import Subscriptions, Message, Kind

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriptions
        fields = ['email']

class SendMessageFrom(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']

class SearchKindForm(ModelForm):
    class Meta:
        model = Kind
        fields = ['kind']
