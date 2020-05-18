from django import forms
from .models import Chaussure

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Chaussure
        fields = ['nom','description','img']
