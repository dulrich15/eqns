from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from . import views

router = DefaultRouter()
router.register('equations', views.EquationViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('systems', views.SystemViewSet)
router.register('variables', views.VariableViewSet)
router.register('constants', views.ConstantViewSet)
router.register('units', views.UnitViewSet)
router.register('limitations', views.LimitationViewSet)

equations_router = NestedSimpleRouter(router, 'equations', lookup='equation')
equations_router.register('variables', views.EquationVariableViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(equations_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += urlpatterns + patterns('',
    url(r'^$', views.show_equations),
    url(r'^app/$', views.angular_app),
)