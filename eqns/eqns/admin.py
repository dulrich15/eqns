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
        
    list_display = ['name', 'sympy', 'subject', 'system']
    list_filter = ['subject', 'system']
    filter_horizontal = ['variables', 'constants', 'limitations']
    
site.register(Equation, EquationAdmin)


class SubjectAdmin(ModelAdmin):
    list_display = ['name', 'sort_order']
    
site.register(Subject, SubjectAdmin)


class SystemAdmin(ModelAdmin):
    list_display = ['name', 'sort_order']
    
site.register(System, SystemAdmin)


class LimitationAdmin(ModelAdmin):
    list_display = ['name', 'sort_order']
    
site.register(Limitation, LimitationAdmin)