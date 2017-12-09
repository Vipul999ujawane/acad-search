# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject, Files
# Register your models here.

def verify(modeladmin,request,queryset):
    queryset.update(verified=True)
verify.short_description="Mark selected files as Verified"

def unverify(modeladmin,request,queryset):
    queryset.update(verified=False)
unverify.short_description="Mark selected files as Unverified"

class FileAdmin(admin.ModelAdmin):
    list_display=('file_name','verified','uploader_roll_no','subject')
    search_fields=('uploader_roll_no','file_name')
    list_filter=('verified','uploader_roll_no')
    actions=[verify,unverify]

class SubjectAdmin(admin.ModelAdmin):
    list_display=('subject_name','subject_code','department_code',)
    search_fields=('department_code','subject_code','subject_name')
    list_filter=('department_code',)


admin.site.register(Subject,SubjectAdmin)
admin.site.register(Files,FileAdmin)
