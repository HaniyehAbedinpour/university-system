from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="courses"
    )

def __str__(self):
    return f'{self.name} | {self.code}'