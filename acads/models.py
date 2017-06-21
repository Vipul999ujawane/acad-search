# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import os
# Create your models here.

def get_file_path(instance,filename):
    return (settings.MEDIA_ROOT+'/'+instance.subject.department_code+'/'+instance.subject.subject_code+'/'+filename)

class Subject(models.Model):
    department_code=models.CharField(max_length=2,blank=False)
    subject_code=models.CharField(max_length=7,blank=False)
    subject_name=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return u'%s | %s' %(self.subject_code,self.subject_name)

class Files(models.Model):
    file_name=models.CharField(max_length=100,blank=False,verbose_name='Topic')
    files=models.FileField(upload_to=get_file_path,blank=False)
    subject=models.ForeignKey(Subject)
    verified=models.BooleanField(default=False)
    uploader_roll_no=models.CharField(max_length=100,blank=False)
    uploader_email=models.EmailField(blank=False)
    description=models.TextField(blank=False)
    def get_relative_path(self):
        pat=os.path.relpath(self.files.path, settings.MEDIA_ROOT)
        return (settings.MEDIA_URL+pat)
    relative_path=property(get_relative_path)
    class Meta:
        verbose_name='File'
        verbose_name_plural='Files'

    def __str__(self):
        return (self.file_name)
