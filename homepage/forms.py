# forms.py

from django import forms
from .models import ThreeDPrintOrder, LaserEngravingOrder

class ThreeDPrintOrderForm(forms.ModelForm):
    class Meta:
        model = ThreeDPrintOrder
        fields = ['stl_file', 'size_description', 'color']

class LaserEngravingOrderForm(forms.ModelForm):
    class Meta:
        model = LaserEngravingOrder
        fields = ['item_description', 'bmp_file', 'description']
