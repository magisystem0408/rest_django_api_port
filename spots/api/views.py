from rest_framework import generics
from spots.models import Spot
from spots.api.serializers import SpotSerializer


class ListView(generics.ListCreateAPIView):
    queryset =Spot.objects.all().order_by('-id')
    serializer_class =SpotSerializer

