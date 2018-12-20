from django import forms

from .models import Passenger

class DetailsForm(forms.ModelForm):

    class Meta :
        model = Passenger
        fields = ('username', 'Name', 'email', 'password')