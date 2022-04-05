from django import forms
from .models import Natillera


class NatilleraCreateForm(forms.ModelForm):
    class Meta:
        model = Natillera
        fields = ('name', 'monthlyfee')