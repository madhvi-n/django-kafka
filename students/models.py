from django.db import models
from django.core.validators import MinValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(4)])
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['email']),
        ]
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
