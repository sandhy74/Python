from django.db import models

class RoadType(models.Model):
   type = models.CharField(max_length=100)
   

class Road(models.Model):
   name = models.CharField(max_length=100)
   length = models.IntegerField(null=True,blank=True)
   width = models.IntegerField(null=True,blank=True)
   longitude = models.DecimalField(max_digits=15, decimal_places=12)
   latitude = models.DecimalField(max_digits=15, decimal_places=12)
   road_type = models.ForeignKey(RoadType, on_delete = models.CASCADE,null = True, blank = True)
   distance = models.IntegerField(null=True,blank=True)
