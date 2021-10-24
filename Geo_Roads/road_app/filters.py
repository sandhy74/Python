# from rest_framework_gis.filterset import GeoFilterSet
# from rest_framework_gis.filters import GeometryFilter
# from django_filters import filters
# from .models import *

# class RoadFilter(GeoFilterSet):
#     county = filters.CharFilter(method= 'get_road_by_county')


#     class Meta:
#         model = RoadType
#         exclude = ['type']

#     def get_facilities_by_subcounty(self, queryset, name, value ):
#         query_ = Road.objects.filter(pk=value)
#         if query_:
#             obj = query_.first()
#             return queryset.filter(road_type = obj.type)
#         return queryset