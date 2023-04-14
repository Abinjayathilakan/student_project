from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Student_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Age = models.IntegerField()
    Email = models.EmailField()
    Joining_date = models.DateField()
    Qualification = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Mobile_number = models.IntegerField()