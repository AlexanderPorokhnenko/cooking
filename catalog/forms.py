from django.forms import ModelForm
from .models import Subscriptions, Message

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriptions
        fields = ['email']

class SendMessageFrom(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']