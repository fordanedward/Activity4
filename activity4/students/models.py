from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enrolled_date = models.DateField()
    email = models.EmailField()
    grade = models.CharField(max_length=5, null=True, blank=True) # Add a new field for testing

    def __str__(self):
        return self.name

