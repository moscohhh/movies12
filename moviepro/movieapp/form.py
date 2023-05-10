from django import forms
from .models import Load


class MovieForm(forms.ModelForm):
    class Meta:
        model=Load
        fields=['name','description','year','img']