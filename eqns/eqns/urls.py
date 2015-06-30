from django.conf.urls import patterns, url, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('equations', views.EquationViewSet)
router.register('categories', views.CategoryViewSet)
router.register('variables', views.VariableViewSet)
router.register('constants', views.ConstantViewSet)
router.register('units', views.UnitViewSet)

urlpatterns = patterns('', 
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)