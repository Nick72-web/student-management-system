from django.db import models

# Create your models here.
class Student(models.Model):
    Student_No = models.PositiveIntegerField()
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Field_of_study = models.CharField(max_length=50)
    GPA = models.FloatField()
    
    def __str__(self):
        return f'Student: {self.First_name} {self.Last_name}'
    
   