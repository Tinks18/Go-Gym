from django import forms
from .models import Gymslot


class SlotForm(forms.ModelForm):
    class Meta:
        model = Gymslot
        fields = ['firstname', 'lastname', 'slot_date', 'slot_time', 'submit']
