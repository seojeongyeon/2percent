from django import forms
from .models import Photoshop, Contest

class PhotoshopForm(forms.ModelForm):
    class Meta:
        model = Photoshop
        fields = ['title','device', 'color', 'kind', 'method', 'fix','app','photobefore','photoafter', 'explain']

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['image'] 