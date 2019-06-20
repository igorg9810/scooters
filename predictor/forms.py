from django import forms
from .models import Conditions

class ConditionsForm(forms.ModelForm):

    class Meta:
        model = Conditions
        fields = ('timestamp', 'season', 'holiday', 'workday', 'weather', 'temp', 'felt_temp', 'wind', 'humidity')