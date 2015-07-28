from __future__ import division
from __future__ import unicode_literals

import requests

from sympy import solve
from sympy import sympify
from sympy import Eq
from sympy import Symbol

from django.shortcuts import redirect
from django.shortcuts import render


def call_api(ob='equations', pk=None, q=None):
    api_url = 'http://django-apps-dulrich15.c9.io/eqns/api/'

    if pk: # pull the object
        url = api_url + '{}/{}/'.format(ob, pk)
        return requests.get(url).json()
    elif q:
        url = api_url + '{}/?limit=10000&{}'.format(ob, q)
        return requests.get(url).json()['results']
    else: # get the whole list
        url = api_url + '{}/?limit=10000'.format(ob)
        return requests.get(url).json()['results']


def list_equations(request):
    try:
        q = 'page={}'.format(int(request.GET['page']))
    except:
        q = None

    data = call_api(q=q)

    next_page = prev_page = None
    if 'next' in data:
        next_page = pg + 1
    if 'previous' in data:
        prev_page = pg - 1

    context = {
        'eqns': data['results'],
        'next_page' : next_page,
        'prev_page' : prev_page,
    }
    template = 'list_equations.html'
    return render(request, template, context)


def show_equation(request, pk):
    context = {
        'eqn': call_api(pk=pk)
    }
    template = 'show_equation.html'
    return render(request, template, context)


def solve_it(eqn, knowns, x):
    LHS, RHS = eqn['sympy'].split('=')
    e = Eq(sympify(LHS), sympify(RHS))

    voi = Symbol(x['symbol']) # upgrade sympy to 0.7.6 if this throws a unicode error

    vals = dict()
    for k in knowns:
        vals[Symbol(k['symbol'])] = k['value']
    for c in eqn['constants']:
        vals[Symbol(c['symbol'])] = c['value']

    answers = solve(e.subs(vals),voi)
    answer = answers[0]

    return answer.evalf()


def show_solution(request, pk):
    eqn = call_api(pk=pk)

    constants = eqn['constants']
    variables = eqn['variables']

    knowns, unknowns = [], []
    for v in variables:
        val = request.POST.get(v['name'], None)
        try:
            v['value'] = float(val)
            knowns.append(v)
        except:
            v['value'] = val
            unknowns.append(v)

    x = None
    if len(unknowns) == 1:
        x = unknowns[0]
    else:
        for u in unknowns:
            if u['value'] == '?':
                x = u

    if x is None:
        return render(request, 'show_error.html', {})

    x['value'] = solve_it(eqn, knowns, x)

    context = {
        'eqn': eqn,
        'constants': constants,
        'variables': knowns,
        'parameters': knowns + constants,
        'x': x,
    }
    template = 'show_solution.html'
    return render(request, template, context)


def show_solver(request):

# Initialize problem data
    # 41 displacement
    # 42 velocity (final)
    # 43 time
    # 44 initial velocity
    # 45 acceleration
    knowns = []
    for (vpk, val) in [(41,-5),(44,0),(45,-5)]:
        v = call_api(pk=vpk, ob='variables')
        v['value'] = val
        knowns.append(v)
    voi = call_api(pk=42, ob='variables')

# Gather list of potential equations
    # eqnlist = call_api() # this will pull the whole list
    eqnlist = call_api(q='system=2&subject=9')
    solvers = []

# Every time we find an intermediate equation, we need to start over until
# we solve for the variable of interest ... or run out of equations
    while True:

# Cycle through the equation list to find a solver equation
        for eqn in eqnlist:
            unknowns = []
            for v in eqn['variables']:
                if v['id'] not in [k['id'] for k in knowns]:
                    unknowns.append(v)

# We'll know we find a solver if all but one of the variables is known
            x = None
            if len(unknowns) == 1:
                x = unknowns[0]
                x['value'] = solve_it(eqn, knowns, x)
                knowns.append(x)
                solvers.append((eqn, x))
                eqnlist.remove(eqn)
                break

# If variable of interest is known, stop looking. If unknown is still None,
# then we didn't find a solver: stop looking, it is time to give up.
        if voi in knowns or x is None:
            break

# If variable of interest is known then solve it!
    if voi in knowns:
        assert False
        template = 'solver_success.html'

# If variable of interest is not known then give up!
    else:
        template = 'solver_givesup.html'

    context = {}
    return render(request, template, context)


## -- Django REST Framework API support -- ##

from rest_framework.viewsets import *

from models import *
from serializers import *
from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

import django_filters


# class EquationFilter(django_filters.FilterSet):
#     system = django_filters.CharFilter(name="system__name")
#     subject = django_filters.CharFilter(name="subject__name")

#     class Meta:
#         model = Equation
#         fields = ['system', 'subject', 'name']


class EquationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equation.objects.all()
    serializer_class = EquationSerializer

    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter]
    # filter_class = EquationFilter
    filter_fields = ['system', 'subject', 'name']
    search_fields = ['subject__name', 'system__name', 'name']


class VariableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer

    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['name']
    search_fields = ['name', 'unit__name']

    @detail_route(url_path='equations')
    def get_equation_list(self, request, *args, **kwargs):
        equation_list = Equation.objects.filter(variables=self.get_object())
        serializer = EquationSerializer(equation_list, many=True, context={'request': request})
        return Response(serializer.data)


class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['name', 'symbol']
    search_fields = ['name', 'symbol']

    @detail_route(url_path='variables')
    def get_variables_list(self, request, *args, **kwargs):
        variable_list = Variable.objects.filter(unit=self.get_object())
        serializer = VariableSerializer(variable_list, many=True, context={'request': request})
        return Response(serializer.data)


# class VariableList(generics.ListCreateAPIView):
#     queryset = Variable.objects.all()
#     serializer_class = VariableSerializer

#     filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter)
#     search_fields = ['name']


# class VariableDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Variable.objects.all()
#     serializer_class = VariableSerializer


# class VariableEquationList(generics.ListCreateAPIView):
#     queryset = Equation.objects.filter(variables=pk)
#     serializer_class = EquationSerializer

#     def get(self, request, *args, **kwargs):
#             snippet = self.get_object()
#             return Response(snippet.highlighted)
