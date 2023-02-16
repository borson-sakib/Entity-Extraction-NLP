from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from  .utils import *

from .models import *

from bs4 import BeautifulSoup


# Create your views here.
import requests
import json
import environ
# Create your views here.



def index(request):

    if(request.method == "POST"):
        text = request.POST['texttoentity']

        html = naturalLP(text)
        text = naturalLPlist(text)
        soup = BeautifulSoup(html, 'html.parser')
        # div = soup.find('div',{'class':'entities'})
        div = soup.find('mark')

        # for tag in soup(['mark', 'span']):
        #     tag.decompose()
        # div = soup.find('div')

        print(type(div))
        print(div)
        return render(request,'base.html',{'html':div,'text':text})

    html = None
    text = None
    return render(request,'base.html',{'html':html,'text':text})

def index2(request):

    return render(request,'xyz.html')  

