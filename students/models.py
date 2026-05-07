from django.db import models

    
from departments.models import Department

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20,unique=True)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    