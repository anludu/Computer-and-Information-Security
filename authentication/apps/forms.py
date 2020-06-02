from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import ModelForm
from .models import Application


class ApplicationForm(ModelForm):
    name = forms.CharField(label="Nombre de la Aplicación")

    class Meta:
        model = Application
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'

