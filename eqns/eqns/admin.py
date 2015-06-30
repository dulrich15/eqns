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
    def nbr_vars(self, obj):
        return obj.variables.count()
        
    list_display = ['name', 'sympy', 'category']
    list_filter = ['category']
    filter_horizontal = ['variables', 'constants']
    
site.register(Equation, EquationAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'sort_order']
    
site.register(Category, CategoryAdmin)