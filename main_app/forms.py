from django import forms
from .models import Drink, Journal


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'recipe']

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'entry']
