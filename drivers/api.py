from .serializers import *
from drivers.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class DriversViewSet(viewsets.ModelViewSet):
    serializer_class = DriversSerializer
    queryset = Drivers.objects.all()
    def get(self, format=None):

        Drivers = Drivers.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)