from .models import Pay_nails
from django.forms import ModelForm


class Pay_nailsForm(ModelForm):
    class Meta:
        model = Pay_nails
        fields = ['nails_for_day']
