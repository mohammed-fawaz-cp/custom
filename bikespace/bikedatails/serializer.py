#create a serializer for the models
from rest_framework import serializers
from bikedatails.models import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

#class to update the data

class ResourceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'
        #allow field to be optional
        extra_kwargs = {
            'name': {'required': False},
            'rating': {'required': False},
            'price': {'required': False},
            'location': {'required': False},
            'image': {'required': False},
            'isfavorite': {'required': False},
        }