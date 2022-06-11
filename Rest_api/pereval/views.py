from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
import traceback
import sys
from django.utils import timezone


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


class SubmitDataListView(generics.ListAPIView):
    serializer_class = SubmitDataDetailSerializer

    def get_queryset(self):
        queryset = SubmitData.objects.all()
        email = self.request.query_params.get('user__email')
        if email is not None:
            email = email.replace('<', '')
            email = email.replace('>', '')
            queryset = queryset.filter(email=email)
        return queryset



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

                submitdata_obj = SubmitData.objects.all().order_by('-id')[0]
                try:
                    if User.objects.filter(email=submitdata_obj.email)[0]:
                        user = User.objects.filter(email=submitdata_obj.email)[0]
                    else:
                        user = User.objects.create(email=submitdata_obj.email, phone=submitdata_obj.phone, fam=submitdata_obj.fam, name=submitdata_obj.name, otc=submitdata_obj.otc)
                except IndexError:
                    user = User.objects.create(email=submitdata_obj.email, phone=submitdata_obj.phone, fam=submitdata_obj.fam, name=submitdata_obj.name, otc=submitdata_obj.otc)

                coords = Coords.objects.create(latitude=submitdata_obj.latitude, longitude=submitdata_obj.longitude, height=submitdata_obj.height)
                images = PerevalImages.objects.create(data=submitdata_obj.data, title_img=submitdata_obj.title_img)
                perevaladded = PerevalAdded.objects.create(submitdata=submitdata_obj, beauty_title=submitdata_obj.beauty_title, title=submitdata_obj.title, other_titles=submitdata_obj.other_titles, connect=submitdata_obj.connect, add_time=submitdata_obj.add_time, coord=coords, level_winter=submitdata_obj.level_winter, level_summer=submitdata_obj.level_summer, level_autumn=submitdata_obj.level_autumn, level_spring=submitdata_obj.level_spring, user=user)
                perevalareas = PerevalAreas.objects.create(parent=perevaladded, title=submitdata_obj.title, status='new')
                perevaladdperevalimages = PerevalAddedPerevalImages.objects.create(pereval_added=perevaladded, pereval_images=images)

                return JsonResponse({"status": 200, "message": "null", "id": perevaladded.submitdata.id})
            return JsonResponse({"status": 400, "message": "Bad Request", "id": "null"})
        except Exception as ex:
            exc_info = sys.exc_info()
            message = ''.join(traceback.format_exception(*exc_info))
            return JsonResponse({"status": 500, "message": message, "id": "null"})


@csrf_exempt
def submitdata_id(request, pk):
    if request.method == 'GET':
        submitdata_obj = SubmitData.objects.filter(id=pk)[0]
        serializer1 = SubmitDataDetailSerializer(submitdata_obj)
        perevalareas_obj = PerevalAreas.objects.filter(parent=submitdata_obj.id)[0]
        serializer2 = PerevalAreasDetailSerializer(perevalareas_obj)
        return JsonResponse({**serializer1.data, **serializer2.data}, safe=False)

    elif request.method == 'PATCH':
        try:
            data = JSONParser().parse(request)
            serializer = SubmitDataDetailSerializer(data=data)
            if serializer.is_valid() and PerevalAreas.objects.filter(parent=pk)[0].status != 'new':
                submitdata_obj = SubmitData.objects.filter(id=pk)[0]
                submitdata_obj.beauty_title = data['beauty_title']
                submitdata_obj.title = data['title']
                submitdata_obj.other_titles = data['other_titles']
                submitdata_obj.connect = data['connect']
                submitdata_obj.add_time = timezone.now()
                submitdata_obj.latitude = data['latitude']
                submitdata_obj.longitude = data['longitude']
                submitdata_obj.height = data['height']
                submitdata_obj.level_winter = data['level_winter']
                submitdata_obj.level_summer = data['level_summer']
                submitdata_obj.level_autumn = data['level_autumn']
                submitdata_obj.level_spring = data['level_spring']
                if data['data'] != '':
                    submitdata_obj.data = data['data']
                submitdata_obj.title_img = data['title_img']
                submitdata_obj.save()

                perevaladded = PerevalAdded.objects.filter(submitdata=pk)[0]
                perevaladded.beauty_title = submitdata_obj.beauty_title
                perevaladded.title = submitdata_obj.title
                perevaladded.other_titles = submitdata_obj.other_titles
                perevaladded.connect = submitdata_obj.connect
                perevaladded.add_time = submitdata_obj.add_time
                perevaladded.latitude = submitdata_obj.latitude
                perevaladded.longitude = submitdata_obj.longitude
                perevaladded.height = submitdata_obj.height
                perevaladded.level_winter = submitdata_obj.level_winter
                perevaladded.level_summer = submitdata_obj.level_summer
                perevaladded.level_autumn = submitdata_obj.level_autumn
                perevaladded.level_spring = submitdata_obj.level_spring
                perevaladded.save()

                coords = Coords.objects.filter(id=perevaladded.coord.id)[0]
                coords.latitude = submitdata_obj.latitude
                coords.longitude = submitdata_obj.longitude
                coords.height = submitdata_obj.height
                coords.save()

                perevaladdedperevalimages = PerevalAddedPerevalImages.objects.filter(pereval_added=perevaladded.submitdata.id)[0]

                perevalimages = PerevalImages.objects.filter(id=perevaladdedperevalimages.pereval_images.id)[0]
                perevalimages.data = submitdata_obj.data
                perevalimages.title_img = submitdata_obj.title_img
                perevalimages.save()

                perevalareas = PerevalAreas.objects.filter(parent=pk)[0]
                perevalareas.title = submitdata_obj.title
                perevalareas.save()

                return JsonResponse({"state": 1, "message": 'null'})
            elif PerevalAreas.objects.filter(parent=pk)[0].status == 'new':
                return JsonResponse({"state": 0, "message": 'This application is not new.'})
            return JsonResponse({"state": 0, "message": "Bad Request"})
        except Exception as ex:
            exc_info = sys.exc_info()
            message = ''.join(traceback.format_exception(*exc_info))
            return JsonResponse({"state": 0, "message": message})
