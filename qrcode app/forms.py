from django import forms
from .models import QRCodeData

class QRCodeDataForm(forms.ModelForm):
    class Meta:
        model = QRCodeData
        fields = ['data']
