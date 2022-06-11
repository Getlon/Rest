from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('PerevalAdded/add/', PerevalAddedCreateView.as_view()),
    path('User/add/', UserCreateView.as_view()),
    path('PerevalAreas/add/', PerevalAreasCreateView.as_view()),
    path('PerevalImages/add/', PerevalImagesCreateView.as_view()),
    path('SprActivitiesTypes/add/', SprActivitiesTypesCreateView.as_view()),
    path('Coords/add/', CoordsCreateView.as_view()),
    path('PerevalAddedPerevalImages/add/', PerevalAddedPerevalImagesCreateView.as_view()),
    path('SubmitData/', SubmitDataListView.as_view()),
    path('SubmitData/', submitdata),
    path('SubmitData/<int:pk>/', submitdata_id),

]
