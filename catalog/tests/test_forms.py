from django.test import TestCase
from catalog.forms import SubscribeForm, SendMessageFrom

class SubscribeFormTest(TestCase):


    def test_subscribe_form_field(self):
        form = SubscribeForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')


class SendMessageFormTest(TestCase):


    def test_send_message_form_field(self):
        form = SendMessageFrom()
        self.assertTrue(form.fields['name'].label == 'Name' and form.fields['email'].label == 'Email' and form.fields['subject'].label == 'Subject'
                        and form.fields['message'].label == 'Message')

    def test_send_message_dict(self):
        form = SendMessageFrom({'csrfmiddlewaretoken': ['bababababa'], 'name': ['aaa'], 'email': ['siemens@gmail.com'], 'subject': ['bbb'], 'message': ['sadasd']})
        self.assertFalse(form.is_valid())

