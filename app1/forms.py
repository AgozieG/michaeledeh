# myapp/forms.py

from django import forms

class FileUploadForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField()