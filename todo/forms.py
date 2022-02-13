from django import forms
from .models import Itens

class ItemForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ['name', 'done']
