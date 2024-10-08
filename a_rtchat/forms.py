from django.forms import ModelForm
from django import forms
from a_rtchat.models import GroupMessage

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'p-4 text-black', 'max_length': '300', 'autofocus': True})
        }