import os
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
import json

#create a api to push bike data
from rest_framework import viewsets
from bikedatails.models import Bike
from bikedatails.serializer import BikeSerializer,ResourceUpdateSerializer
from rest_framework.views import APIView

from bikespace import settings

class BikeViewSet(APIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    def get(self, request):
        returndata = Bike.objects.all()
        serializer = BikeSerializer(returndata, many=True)
        return Response(serializer.data)
    

#class to upload data by the user

class UploadData(APIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    def post(self, request):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class DeleteData(generics.DestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    def perform_destroy(self, instance):
        # If the instance has an image field, delete the image file
        if instance.image:
            # Construct the full file path
            image_path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
            # Delete the file if it exists
            if os.path.isfile(image_path):
                os.remove(image_path)
        # Delete the instance
        instance.delete()


# function to edit the data




class Update(generics.RetrieveUpdateAPIView):
    queryset = Bike.objects.all()
    serializer_class = ResourceUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Retain previous values for unedited fields and fields explicitly set to None
        updated_data = {}
        for field in serializer.fields:
            if field not in request.data or request.data[field] is None:
                updated_data[field] = getattr(instance, field)

        # Update the instance with the request data
        self.perform_update(serializer)

        # Merge the updated data with the serializer data
        updated_data.update(serializer.data)

        return Response(updated_data)