from django.db import models
from django.conf import settings
from exercises.models import Exercise
import uuid

class PersonalWorkoutPlan(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ManyToManyField(Exercise)
    repetition = models.PositiveIntegerField() 
    set = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user) + " personal workout plan"
    

class WeightMeasurement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    measured_at = models.DateTimeField(auto_now_add=True)

class FitnessGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2)
    target_date = models.DateField()
    exercise_achievements = models.TextField()