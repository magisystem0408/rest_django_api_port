from rest_framework import serializers
from spots.models import Spot


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model =Spot
        fields ='__all__'