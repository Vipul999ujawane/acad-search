# -- coding: utf-8 --

from django import forms
from .models import Files,Subject
from django.forms import ModelForm
class UploadForm(ModelForm):
    class Meta:
        model=Files
        fields=['subject','file_name','description','files','uploader_roll_no','uploader_email',] 
