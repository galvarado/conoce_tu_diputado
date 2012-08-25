# coding: utf-8
import json
import operator

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db.models import Q

from main.models import Representative

def index(request):
    '''
    Show index page
    '''
    return render_to_response('index.html', RequestContext(request))

def map(request):
    '''
    Show map page
    '''
    return render_to_response('map.html', RequestContext(request))

def get_deputies(request):
    '''
    Retrive deputies table when user search in map
    '''
    aaData = []
    start = request.POST.get('iDisplayStart')
    display_length = request.POST.get('iDisplayLength')
    end = start + display_length
    search = request.POST.get('sSearch')
    representatives = Representative.objects.filter(entity=search)
    count = representatives.count()

    for representative in representatives[start:end]:
        aaData.append([
            '%s %s' % (representative.name, representative.lastname),
            representative.district,
            representative.party,
            '<a><img class=contact src=static/main/images/contact_icon.jpg /></a>',
        ])
    data = {
        'iTotalRecords': count,
        'iDisplayStart': start,
        'iDisplayLength': display_length,
        'iTotalDisplayRecords': count,
        'aaData':aaData
    }
    return HttpResponse(json.dumps(data))

def search(request):
    '''
    Show search page
    '''
    return render_to_response('search.html', RequestContext(request))

def get_deputies_search(request):
    '''
    Retrive deputies specific search
    '''
    aaData = []
    start = request.POST.get('iDisplayStart')
    display_length = request.POST.get('iDisplayLength')
    end = display_length
    search = request.POST.get('sSearch', None)
    if search:

        search = search.split(' ')

        fields = ('sex', 'name', 'lastname', 'party', 'election_type', 'entity', 'district', 'circunscription', 'phone', 'extension', 'email', 'twitter', 'commissions', 'bio', 'patrimony', 'answer', 'answer_why', 'suplent', 'status')

        # Query to filter records
        _query = """SELECT * FROM main_representative WHERE 1"""

        args_to_append = []

        for arg in search:
            _query += """ AND ("""

            i = 0

            for field in fields:
                if i > 0:
                    _query += " OR "

                _query += field + " LIKE %s"
                args_to_append.append(arg)
                i = i + 1

            _query += """)"""

        _query += """ LIMIT %s,%s"""

        args_to_append.append(start)
        args_to_append.append(end)

        representatives = Representative.objects.raw(_query, args_to_append)
        # Query to obtain total count
        _query = """SELECT * FROM main_representative WHERE 1"""

        args_to_append = []

        for arg in search:
            _query += """ AND ("""

            i = 0

            for field in fields:
                if i > 0:
                    _query += " OR "

                _query += field + " LIKE %s"
                args_to_append.append(arg)
                i = i + 1

            _query += """)"""
        count = len(list(Representative.objects.raw(_query, args_to_append)))
        for representative in representatives:
            aaData.append([
                '%s %s' % (representative.name, representative.lastname),
                representative.party,
                representative.entity,
                representative.district,
                representative.election_type,
                '<a><img class=contact src=static/main/images/contact_icon.jpg /></a>',
            ])

    else:
        representatives = Representative.objects.all()
        count = representatives.count()

        for representative in representatives[start:end]:
            aaData.append([
                '%s %s' % (representative.name, representative.lastname),
                representative.party,
                representative.entity,
                representative.district,
                representative.election_type,
                '<a><img class=contact src=static/main/images/contact_icon.jpg /></a>',
            ])

    data = {
        'iTotalRecords': count,
        'iDisplayStart': start,
        'iDisplayLength': display_length,
        'iTotalDisplayRecords': count,
        'aaData':aaData
    }
    return HttpResponse(json.dumps(data))
