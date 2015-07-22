from __future__ import division
from __future__ import unicode_literals

import requests

from django.shortcuts import redirect
from django.shortcuts import render

def list_equations(request):
    try:
        pg = int(request.GET['page'])
    except:
        pg = 1

    url = 'http://{}/eqns/api/?page={}'.format(request.get_host().split(':')[0], pg)
    data = requests.get(url).json()

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
    url = 'http://{}/eqns/api/{}'.format(request.get_host().split(':')[0], pk)
    eqn = requests.get(url).json()

    context = {
        'eqn': eqn,
    }
    template = 'show_equation.html'


    if request.POST:
        parameters = eqn['constants']
        x = eqn['variables'][:] # copy this list
        for v in eqn['variables']:
            print v
            if v['name'] not in request.POST:
                v['value'] = 'Not given'
                paramters.append(v)
            else: # we have a variable
                if request.POST[v['name']] == "?":
                    x = [v]
                else: # we have a value
                    try:
                        v['value'] = float(request.POST[v['name']])
                        parameters.append(v)
                        x.remove(v)
                    except: # error: input is not a float
                        v['value'] = 'Not Given'
                        parameters += [v]

        if len(x) != 1:
            return render(request, 'show_error.html', {})
        else:
            x = x[0]

        x['value'] = 100

        context.update({
            'pst': request.POST,
            'parameters': parameters,
            'x': x,
        })
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
