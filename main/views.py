# coding: utf-8
import json

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.db.models import Q

def index(request):
    return render_to_response('index.html', RequestContext(request))