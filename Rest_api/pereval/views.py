from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
import traceback
import sys


class PerevalAddedCreateView(generics.CreateAPIView):
    serializer_class = PerevalAddedDetailSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class PerevalAreasCreateView(generics.CreateAPIView):
    serializer_class = PerevalAreasDetailSerializer


class PerevalImagesCreateView(generics.CreateAPIView):
    serializer_class = PerevalImagesDetailSerializer


class SprActivitiesTypesCreateView(generics.CreateAPIView):
    serializer_class = SprActivitiesTypesDetailSerializer


class CoordsCreateView(generics.CreateAPIView):
    serializer_class = CoordsDetailSerializer


class PerevalAddedPerevalImagesCreateView(generics.CreateAPIView):
    serializer_class = PerevalAddedPerevalImagesDetailSerializer


class SubmitDataCreateView(generics.CreateAPIView):
    serializer_class = SubmitDataDetailSerializer


@csrf_exempt
def submitdata(request):
    if request.method == 'GET':
        submitdata = SubmitData.objects.all()
        serializer = SubmitDataDetailSerializer(submitdata, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            serializer = SubmitDataDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # continue here

                submitdata_obj = SubmitData.objects.all().order_by('-id')[0]

                user = User.objects.create(email=submitdata_obj.email, phone=submitdata_obj.phone, fam=submitdata_obj.fam, name=submitdata_obj.name, otc=submitdata_obj.otc)
                coords = Coords.objects.create(latitude=submitdata_obj.latitude, longitude=submitdata_obj.longitude, height=submitdata_obj.height)
                images = PerevalImages.objects.create(data=submitdata_obj.data, title_img=submitdata_obj.title_img)
                perevaladded = PerevalAdded.objects.create(date_added=submitdata_obj.add_time, beauty_title=submitdata_obj.beauty_title, title=submitdata_obj.title, other_titles=submitdata_obj.other_titles, connect=submitdata_obj.connect, add_time=submitdata_obj.add_time, coord=coords, level_winter=submitdata_obj.level_winter, level_summer=submitdata_obj.level_summer, level_autumn=submitdata_obj.level_autumn, level_spring=submitdata_obj.level_spring)
                perevalareas = PerevalAreas.objects.create(parent=perevaladded, title=submitdata_obj.title, status='new')
                perevaladdperevalimages = PerevalAddedPerevalImages.objects.create(pereval_added=perevaladded, pereval_images=images)

                return JsonResponse({"status": 200, "message": "null", "id": serializer.data['id']})
            return JsonResponse({"status": 400, "message": "Bad Request", "id": "null"})
        except Exception as ex:
            exc_info = sys.exc_info()
            message = ''.join(traceback.format_exception(*exc_info))
            return JsonResponse({"status": 500, "message": message, "id": "null"})
