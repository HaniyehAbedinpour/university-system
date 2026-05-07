from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20,unique=True)
    

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f'{self.name} | {self.student_id}'
    