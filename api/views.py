from api.serialization import *
from rest_framework import generics, authentication, permissions


# Create your views here.


class ViewRoute(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = SerRoute


class ViewCoordinatesOnRoute(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SerCoordinates

    def get_queryset(self):
        return Coordinates.objects.filter(route=self.kwargs['route_id']).distinct()
