from rest_framework import routers
from road_app.views import *
from django.urls import include, path

router = routers.DefaultRouter()
router.register('roadtype/', RoadTypeViewSet)
router.register('road/', RoadView)

urlpatterns = [
   path('', include(router.urls)),
]