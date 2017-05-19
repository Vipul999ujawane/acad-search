# -- coding: utf-8 --

from django import forms
from models import Files,Subject
from django.forms import ModelForm
class UploadForm(ModelForm):
    class Meta:
        model=Files
        fields=['uploader_roll_no','uploader_email','subject','description','file_name','files',]
