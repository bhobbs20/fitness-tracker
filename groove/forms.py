
from .models import Groove
from django import forms

class GrooveForm(forms.ModelForm):
    class Meta:
        model = Groove
        fields = [ 'groove', 'duration', 'date']
       