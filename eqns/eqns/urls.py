from django.conf.urls import patterns, url, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('equations', views.EquationViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('systems', views.SystemViewSet)
router.register('variables', views.VariableViewSet)
router.register('constants', views.ConstantViewSet)
router.register('units', views.UnitViewSet)
router.register('limitations', views.LimitationViewSet)

urlpatterns = patterns('', 
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)