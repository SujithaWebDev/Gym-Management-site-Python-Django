from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['fname','lname','phone','email','gender','subscription','date','gender']