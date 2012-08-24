# coding: utf-8
import json

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.db.models import Q

def index(request):
    return render_to_response('index.html', RequestContext(request))

def get_deputies(request):
    '''
    Retrive deputies table
    '''
    aaData = []
    start = request.POST.get('iDisplayStart')
    display_length = request.POST.get('iDisplayLength')
    end = start + display_length
    search = request.POST.get('sSearch')
    users = []
    count = users.count()

    for user in users[start:end]:
        group = 'Sin asignar' if user.profile.group is None else user.profile.group.name
        aaData.append([
            user.username,
            user.email,
            group,
            '<input type="checkbox" data-id="%s">' % user.pk,
        ])
    data = {
        "iTotalRecords": count,
        "iDisplayStart": start,
        "iDisplayLength": 0,
        "iTotalDisplayRecords": count,
        "aaData":aaData
    }
    return HttpResponse(json.dumps(data))