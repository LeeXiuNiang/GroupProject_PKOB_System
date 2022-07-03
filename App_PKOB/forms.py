from django import forms
from .models import *

class VictimCreate(forms.ModelForm):
    class Meta:
        model = Victim
        fields = '__all__'

class RequestCreate(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class DeclineCreate(forms.ModelForm):
    class Meta:
        model = Decline
        fields = '__all__'

class ReceiveCreate(forms.ModelForm):
    class Meta:
        model = Receive
        fields = '__all__'