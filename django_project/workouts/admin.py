from django.contrib import admin
from .models import PersonalWorkoutPlan, FitnessGoal, WeightMeasurement


admin.site.register(PersonalWorkoutPlan)
admin.site.register(FitnessGoal)
admin.site.register(WeightMeasurement)