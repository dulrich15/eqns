from __future__ import division
from __future__ import unicode_literals

from django.db.models import *


class Unit(Model):
    symbol = CharField(max_length=200)
    name = CharField(max_length=200, null=True, blank=True)
    quantity = CharField(max_length=200, null=True, blank=True)
    equivalent = CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.name if self.name else self.symbol
        
    class Meta:
        ordering = ['symbol']
        
        
class Variable(Model):
    symbol = CharField(max_length=200)
    name = CharField(max_length=200, null=True, blank=True)
    unit = ForeignKey(Unit, null=True, blank=True)
    
    def __unicode__(self):
        return '{self.symbol} = {self.name}'.format(self=self)
        
    class Meta:
        ordering = ['symbol']
        
        
class Constant(Model):
    symbol = CharField(max_length=200)
    name = CharField(max_length=200, null=True, blank=True)
    value = FloatField()
    unit = ForeignKey(Unit, null=True, blank=True)
    
    def __unicode__(self):
        return '{self.symbol} = {self.value:.3g} {self.unit} ({self.name})'.format(self=self)
        
    class Meta:
        ordering = ['symbol']
    
    
class Category(Model):
    name = CharField(max_length=200)
    sort_order = PositiveSmallIntegerField(default=0)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name_plural = 'categories'
        
        
class Equation(Model):
    name = CharField(max_length=200)
    category = ForeignKey(Category)
    sympy = TextField()
    latex = TextField(null=True, blank=True)
    variables = ManyToManyField(Variable, blank=True)
    constants = ManyToManyField(Constant, blank=True)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['category', 'name']
        
        
