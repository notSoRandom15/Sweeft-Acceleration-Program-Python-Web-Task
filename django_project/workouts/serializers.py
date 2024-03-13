from rest_framework import serializers
from .models import PersonalWorkoutPlan, WeightMeasurement, FitnessGoal
from exercises.serializers import ExerciseSerializer

class PersonalWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalWorkoutPlan
        fields = ['id', 'exercise', 'repetition', 'set', 'duration', 'distance']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['exercise'] = ExerciseSerializer(instance.exercise.all(), many=True).data
        return data


class WeightMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightMeasurement
        fields = ['weight', 'measured_at']

class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = ['goal_weight', 'target_date', 'exercise_achievements']