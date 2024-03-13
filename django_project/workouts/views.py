from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PersonalWorkoutPlan, WeightMeasurement, FitnessGoal
from .serializers import PersonalWorkoutPlanSerializer, WeightMeasurementSerializer, FitnessGoalSerializer
from .permissions import IsOwnerOrReadOnly

class PersonalWorkoutPlanList(generics.ListCreateAPIView):
    queryset = PersonalWorkoutPlan.objects.all()
    serializer_class = PersonalWorkoutPlanSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PersonalWorkoutPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalWorkoutPlan.objects.all()
    serializer_class = PersonalWorkoutPlanSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class WeightMeasurementListCreate(generics.ListCreateAPIView):
    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightMeasurementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WeightMeasurementRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightMeasurementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class FitnessGoalListCreate(generics.ListCreateAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FitnessGoalRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]