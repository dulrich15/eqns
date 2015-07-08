from __future__ import division
from __future__ import unicode_literals

import requests

from django.shortcuts import redirect
from django.shortcuts import render

def show_equations(request):
    base_url = 'http://' + request.get_host().split(':')[0]
    r = requests.get(base_url + '/eqns/api/equations/')
    json = r.json
    context = { 'json': json }
    template = 'show_equations.html'
    return render(request, template, context)

def angular_app(request):
    context = {}
    template = 'angular_app.html'
    return render(request, template, context)

## -- Django REST Framework API support -- ##

from rest_framework.viewsets import *

from models import *
from serializers import *


class UnitViewSet(ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class VariableViewSet(ReadOnlyModelViewSet):
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer


class ConstantViewSet(ReadOnlyModelViewSet):
    queryset = Constant.objects.all()
    serializer_class = ConstantSerializer


class SubjectViewSet(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SystemViewSet(ReadOnlyModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class LimitationViewSet(ReadOnlyModelViewSet):
    queryset = Limitation.objects.all()
    serializer_class = LimitationSerializer


class EquationViewSet(ReadOnlyModelViewSet):
    queryset = Equation.objects.all()
    serializer_class = EquationSerializer
