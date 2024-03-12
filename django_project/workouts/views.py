from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PersonalWorkoutPlan
from .serializers import PersonalWorkoutPlanSerializer
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
