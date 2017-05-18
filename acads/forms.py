# -- coding: utf-8 --

from django import forms
from models import Files,Subject
from django.forms import ModelForm
class UploadForm(ModelForm):
    class Meta:
        model=Files
        fields=['file_name','files','subject','uploader_roll_no','uploader_email']
