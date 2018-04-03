from rest_framework.serializers import *
from api.models import *


class SerRoute(ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class SerCoordinates(ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('name', 'easting', 'northing')
