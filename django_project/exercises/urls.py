# exercises/urls.py
from django.urls import path
from .views import ExerciseList, ExerciseDetail
import uuid


urlpatterns = [
    path('exercises/', ExerciseList.as_view(), name='exercise-list'),
    path('exercises/<uuid:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),
]
