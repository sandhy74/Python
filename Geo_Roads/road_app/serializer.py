from rest_framework import serializers
from road_app.models import *
class RoadTypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = RoadType
       fields = '__all__'


class RoadSerializer(serializers.ModelSerializer):
   class Meta:
       model = Road
       fields ='__all__'