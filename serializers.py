from rest_framework.serializers import *
from models import *


class UnitSerializer(ModelSerializer):
# class UnitSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Unit


class VariableSerializer(ModelSerializer):
    unit = UnitSerializer()
# class VariableSerializer(HyperlinkedModelSerializer):
#     unit = HyperlinkedRelatedField(view_name='unit-detail', read_only=True)

    class Meta:
        model = Variable


class ConstantSerializer(ModelSerializer):
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
# class EquationSerializer(HyperlinkedModelSerializer):
#     subject = SubjectSerializer()
#     system = SystemSerializer()
#     variables = HyperlinkedRelatedField(view_name='variable-detail', many=True, read_only=True)
#     constants = ConstantSerializer(many=True)
#     limitations = LimitationSerializer(many=True)

    class Meta:
        model = Equation
        # fields = ['name', 'sympy', 'latex', 'subject', 'system', 'variables', 'constants', 'limitations']

