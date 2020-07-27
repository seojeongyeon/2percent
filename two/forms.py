from django import forms
from .models import Photoshop

class PhotoshopForm(forms.ModelForm):
    class Meta:
        model = Photoshop
        fields = ['device', 'color', 'kind', 'method', 'fix','app','photobefore','photoafter', 'explain']