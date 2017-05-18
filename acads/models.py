# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import os
# Create your models here.

def get_file_path(instance,filename):
    return (settings.MEDIA_ROOT+'/'+instance.subject.departement_code+'/'+instance.subject.subject_code+'/'+filename)

class Subject(models.Model):
    departement_code=models.CharField(max_length=2,blank=False)
    subject_code=models.CharField(max_length=7,blank=False)
    subject_name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return u'%s | %s' %(self.subject_code,self.subject_name)

class Files(models.Model):
    file_name=models.CharField(max_length=100,blank=False)
    files=models.FileField(upload_to=get_file_path,blank=False)
    subject=models.ForeignKey(Subject)
    verified=models.BooleanField(default=False)
    uploader_roll_no=models.CharField(max_length=100,blank=False)
    uploader_email=models.EmailField(blank=False)

    def __str__(self):
        return (self.file_name)
