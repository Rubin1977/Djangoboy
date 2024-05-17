from django import forms
from .models import Ceny

class AddCenyForm(forms.ModelForm):
    class Meta:
        model = Ceny
        fields = ('url', )
