from __future__ import division
from __future__ import unicode_literals

import requests

from sympy import solve
from sympy import sympify
from sympy import Eq
from sympy import Symbol

from django.shortcuts import redirect
from django.shortcuts import render


api_url = 'http://django-apps-dulrich15.c9.io/eqns/api/'


def call_eqn_api(pk=None, pg=1):
    if pk: # pull the equation
        url = api_url + '{}/'.format(pk)
    else: # get a list instead
        url = api_url + '?page={}'.format(pg)
    return requests.get(url).json()


def list_equations(request):
    try:
        pg = int(request.GET['page'])
    except:
        pg = 1

    data = call_eqn_api(pg=pg)

    next_page = prev_page = None
    if data['next']:
        next_page = pg + 1
    if data['previous']:
        prev_page = pg - 1

    context = {
        'eqns': data['results'],
        'next_page' : next_page,
        'prev_page' : prev_page,
    }
    template = 'index.html'
    return render(request, template, context)


def show_equation(request, pk):
    context = {
        'eqn': call_eqn_api(pk=pk)
    }
    template = 'show_equation.html'
    return render(request, template, context)


def show_solution(request, pk):
    eqn = call_eqn_api(pk=pk)
    LHS, RHS = eqn['sympy'].split('=')
    e = Eq(sympify(LHS), sympify(RHS))
    # voi = None

    variables = []
    vals = dict()
    for v in eqn['variables']:
        if v['name'] in request.POST: # really, they all ought to be...
            val = request.POST[v['name']]
            if val == '?':
                voi = Symbol(v['symbol'])
                unknown = v
            else:
                try:
                    value = float(val)
                    vals[Symbol(v['symbol'])] = value
                    v['value'] = value
                except:
                    v['value'] = 'Not given'
                variables.append(v)

    constants = []
    for c in eqn['constants']:
        vals[Symbol(c['symbol'])] = c['value']
        constants.append(c)

    answers = solve(e.subs(vals),voi)
    answer = answers[0]
    unknown['value'] = answer

    context = {
        'eqn': eqn,
        'constants': constants,
        'variables': variables,
        'parameters': variables + constants,
        'x': unknown,
    }
    template = 'show_solution.html'
    return render(request, template, context)


## -- Django REST Framework API support -- ##


from rest_framework.viewsets import *

from models import *
from serializers import *
from rest_framework import generics


class EquationList(generics.ListCreateAPIView):
    queryset = Equation.objects.all()
    serializer_class = EquationSerializer


class EquationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equation.objects.all()
    serializer_class = EquationSerializer
