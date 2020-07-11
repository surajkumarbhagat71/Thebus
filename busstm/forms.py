from django import forms
from .models import *

class UserSingupForm(forms.ModelForm):
    class Meta:
        model = UserSingup
        fields = '__all__'


class OnerSignUpForm(forms.ModelForm):
    class Meta:
        model = OnerSignup
        fields = '__all__'


class Busform(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
