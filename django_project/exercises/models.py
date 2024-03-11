from django.db import models
import uuid

class Exercise(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    instruction = models.TextField()
    muscle_choices = [
        ('legs', 'legs'),
        ('chest', 'chest'),
        ('abs', 'abs'),
        ('biceps', 'biceps'),
        ('triceps', 'triceps'),
    ]
    target_muscles = models.CharField(max_length=10, choices=muscle_choices)

    def __str__(self):
        return self.name
    