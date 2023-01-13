from rest_framework import routers
from .api import MedicionViewSet, MedicionMaxViewSet

routes = routers.DefaultRouter()

routes.register('api/save', MedicionViewSet)
routes.register('api/max', MedicionMaxViewSet)

urlpatterns = routes.urls