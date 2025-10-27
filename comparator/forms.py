from django import forms
from .models import PDFComparision

class PDFComparisionForm(forms.ModelForm):
    class Meta:
        model = PDFComparision
        fields = ['pdf_file_1', 'pdf_file_2']
