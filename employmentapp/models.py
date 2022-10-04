from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=20, null=True)
    second_name = models.CharField(max_length=240, null=True)
    date_of_graduation=models.DateTimeField()
    date_of_employment=models.DateTimeField()
    position=models.CharField(max_length=20, null=True)
    salary=models.IntegerField()

    def __str__(self):
     return self.first_name


