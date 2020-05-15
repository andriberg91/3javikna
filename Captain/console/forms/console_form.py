from django.forms import ModelForm, widgets
from django import forms
from console.models import Console

class ConsoleUpdateForm(ModelForm):
    class Meta:
        model = Console
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
            'detailed_description': widgets.TextInput(attrs={'class': 'form-control'})
        }

class ConsoleCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Console
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-control'})
        }
