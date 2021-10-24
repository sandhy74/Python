from rest_framework import viewsets
from django.shortcuts import render
from road_app.models import *
from road_app.serializer import *
from django.http import HttpResponse, JsonResponse
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
class RoadTypeViewSet(viewsets.ModelViewSet):
   queryset = RoadType.objects.all()
   
   serializer_class = RoadTypeSerializer


class RoadView(viewsets.ModelViewSet):
   queryset = Road.objects.all()
   serializer_class = RoadSerializer

   @action(detail=False, methods=['get'])
   def get_nearest_road(self, request):
        nearest_road = Road.ojects.filter(latitude=request.GET['latitude'],
        longitude=request.GET['longitude'],distance=request.GET['distance'])
        road=nearest_road.values_list('name','road_type')
        nearest_road_list={'road':road}
        return Response(nearest_road_list)

   @action(detail=False, methods=['post'])
   def post(self,request):
        
      serializer=RoadSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         #import pdb;pdb.set_trace()
         self.display(request)
         
         return Response(status=200)
      else:
         print (serializer.errors)
         return Response(status=404) 

   @action(detail=False, methods=['get'])
   def get(self,request):

      country_road=Road.objects.all()
      serializer=RoadSerializer(country_road,many=True)
      return Response(serializer.data , status=200)

   @action(detail=True, methods=['put'])
   def put(self,request,pk):

      country_road = Road.objects.get(pk=id)
      serializer = RoadSerializer(country_road, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   @action(detail=True, methods=['delete'])
   def delete(self, request,pk):


      road= Road.objects.get(pk=id)
      serializer = RoadSerializer(road, data=request.data)
      if serializer.is_valid():
         road.delete()
         return Response(serializer.data)
      return Response(status=status.HTTP_204_NO_CONTENT) 
  

      




