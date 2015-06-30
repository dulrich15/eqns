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

    
class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class EquationViewSet(ReadOnlyModelViewSet):
    queryset = Equation.objects.all()
    serializer_class = EquationSerializer
