# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from acads.forms import UploadForm
from acads.models import Subject,Files
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.core import serializers

# Create your views here.
def upload(request):
    if request.method=='POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
        else:
            print "error"
    else:
        form = UploadForm()
    Sub=['AE','AG','AR','AT','BS','BT','CE','CH','CS','CY','EA','EC','EE',
        'EV','EX','GG','HS','IE','IM','MA','ME','MF','MI','MT','NA','PH','QE','QM']
    return render(request, 'upload.html', {'form': form,'subject':Sub})

def home(request):
    Sub=['AE','AG','AR','AT','BS','BT','CE','CH','CS','CY','EA','EC','EE',
        'EV','EX','GG','HS','IE','IM','MA','ME','MF','MI','MT','NA','PH','QE','QM']
    Year=['1','2','3','4','5','6']
    return render(request,'home.html',{'subject':Sub,'year':Year})
def success(request):
    return render(request,'success.html')

def get_sub_list(request,dept):
    sub=Subject.objects.filter(department_code=dept).order_by('subject_code')
    data=serializers.serialize("json",sub)
    #print data
    return HttpResponse(data, content_type="application/json")

def get_files(request,dept,year):
    q=dept+year
    files=Files.objects.filter(subject__subject_code__contains=q,verified=True)
    #print files
    return render(request,'file.html',{'dept':dept,'year':year,'files':files})
