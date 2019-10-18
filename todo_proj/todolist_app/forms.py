from django import forms
from .models import List


class FormL(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
