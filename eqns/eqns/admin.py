from django.contrib.admin import *
from models import *


class UnitAdmin(ModelAdmin):
    list_display = ['symbol', 'name', 'quantity', 'equivalent']
    
site.register(Unit, UnitAdmin)


class VariableAdmin(ModelAdmin):
    list_display = ['name', 'symbol', 'unit']
    
site.register(Variable, VariableAdmin)


class ConstantAdmin(ModelAdmin):
    list_display = ['name', 'symbol', 'value', 'unit']
    
site.register(Constant, ConstantAdmin)


class EquationAdmin(ModelAdmin):
    list_display = ['name', 'sympy', 'category']
    
site.register(Equation, EquationAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'sort_order']
    
site.register(Category, CategoryAdmin)