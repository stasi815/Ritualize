from django import forms
from .models import Ceremony

class CeremonyForm(forms.ModelForm):
    """ Render and process a form based on the Ceremony model. """

    class Meta:
        model = Ceremony
        fields = ['title', 'content', 'author']
