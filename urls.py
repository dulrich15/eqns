from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.list_equations, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.show_equation, name='show_equation'),
    url(r'^api/$', views.EquationList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.EquationDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
