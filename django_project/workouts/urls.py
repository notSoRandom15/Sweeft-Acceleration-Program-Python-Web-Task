from django.urls import path
from .views import PersonalWorkoutPlanList, PersonalWorkoutPlanDetail

urlpatterns = [
    path('personal-plans/', PersonalWorkoutPlanList.as_view(), name='personal-workout-plan-list'),
    path('personal-plans/<uuid:pk>/', PersonalWorkoutPlanDetail.as_view(), name='personal-workout-plan-detail'),
]
