from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from . import views

# equation_list = views.EquationViewSet.as_view({
#     'get': 'list'
# })
# equation_detail = views.EquationViewSet.as_view({
#     'get': 'retrieve'
# })
# variable_list = views.VariableViewSet.as_view({
#     'get': 'list'
# })
# variable_detail = views.VariableViewSet.as_view({
#     'get': 'retrieve'
# })

router = DefaultRouter()
router.register(r'equations', views.EquationViewSet)
router.register(r'variables', views.VariableViewSet)
router.register(r'units', views.UnitViewSet)

urlpatterns = patterns('',
    url(r'^$', views.list_equations, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.show_equation, name='show_equation'),
    url(r'^(?P<pk>[0-9]+)/solution/$', views.show_solution, name='show_solution'),

    # url(r'^api/equations/$', equation_list, name='equation-list'),
    # url(r'^api/equations/(?P<pk>[0-9]+)/$', equation_detail, name='equation-detail'),
    # url(r'^api/variables/$', variable_list, name='variable-list'),
    # url(r'^api/variables/(?P<pk>[0-9]+)/$', variable_detail, name='variable-detail'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # url(r'^api/variables/(?P<pk>[0-9]+)/equations/$', views.VariableEquationList.as_view()),
)
