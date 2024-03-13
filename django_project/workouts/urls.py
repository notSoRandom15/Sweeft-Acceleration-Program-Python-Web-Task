from django.urls import path
from .views import PersonalWorkoutPlanList, PersonalWorkoutPlanDetail, WeightMeasurementListCreate, WeightMeasurementRetrieveUpdate, FitnessGoalListCreate, FitnessGoalRetrieveUpdate

urlpatterns = [
    path('personal-plans/', PersonalWorkoutPlanList.as_view(), name='personal-workout-plan-list'),
    path('personal-plans/<uuid:pk>/', PersonalWorkoutPlanDetail.as_view(), name='personal-workout-plan-detail'),
    path('weight-measurements/', WeightMeasurementListCreate.as_view(), name='weight-measurement-list'),
    path('weight-measurements/<int:pk>/', WeightMeasurementRetrieveUpdate.as_view(), name='weight-measurement-detail'),
    path('fitness-goals/', FitnessGoalListCreate.as_view(), name='fitness-goal-list'),
    path('fitness-goals/<int:pk>/', FitnessGoalRetrieveUpdate.as_view(), name='fitness-goal-detail'),
]
