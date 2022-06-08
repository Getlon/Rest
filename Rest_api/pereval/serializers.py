from rest_framework import serializers
from .models import *


class PerevalAddedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PerevalAreasDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = '__all__'


class PerevalImagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class SprActivitiesTypesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprActivitiesTypes
        fields = '__all__'


class CoordsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedPerevalImagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAddedPerevalImages
        fields = '__all__'


class SubmitDataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitData
        fields = '__all__'
