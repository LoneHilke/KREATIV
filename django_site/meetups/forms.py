from django import forms
from .models import Participant

class Registrationform(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ['email']
