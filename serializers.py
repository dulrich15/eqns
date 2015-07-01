from rest_framework.serializers import *
from models import *


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        
        
class VariableSerializer(ModelSerializer):
    unit = UnitSerializer()
    
    class Meta:
        model = Variable

        
class ConstantSerializer(ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Constant

        
class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject

class SystemSerializer(ModelSerializer):
    class Meta:
        model = System

        
class LimitationSerializer(ModelSerializer):
    class Meta:
        model = Limitation

        
class EquationSerializer(ModelSerializer):
    subject = SubjectSerializer()
    system = SystemSerializer()
    variables = VariableSerializer(many=True)
    constants = ConstantSerializer(many=True)
    limitations = LimitationSerializer(many=True)

    class Meta:
        model = Equation
        fields = ['name', 'sympy', 'latex', 'subject', 'system', 'variables', 'constants', 'limitations']
    
