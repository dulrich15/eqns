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
