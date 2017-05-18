# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from acads.forms import UploadForm
from acads.models import Subject
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
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
    return render(request, 'upload.html', {'form': form})

def home(request):
    return render(request,'home.html')
def success(request):
    return render(request,'success.html')
