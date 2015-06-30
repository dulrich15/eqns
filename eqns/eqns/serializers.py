from rest_framework.serializers import *
from models import *


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        
        
class VariableSerializer(ModelSerializer):
    unit = HyperlinkedRelatedField(many=True, read_only=True, view_name='unit-detail')
    
    class Meta:
        model = Variable
        fields = ['symbol', 'name', 'unit']
        
        
class ConstantSerializer(ModelSerializer):
    class Meta:
        model = Constant
        # fields = ['symbol', 'name', 'value', 'unit']
        
        
class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'sort_order']
        
        
class EquationSerializer(ModelSerializer):
    category = StringRelatedField(read_only=True)
    # variables = VariableSerializer()
    constants = ConstantSerializer()
    
    class Meta:
        model = Equation
