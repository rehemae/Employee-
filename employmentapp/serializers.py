from rest_framework import serializers
from employmentapp.models import Employee
from django.db import models

class EmployeeSerializer(serializers.ModelSerializer):
    # Meta data is important to serialize the fields in Employee Model
    class Meta:
        model = Employee
        fields = ['first_name', 'second_name', 'date_of_graduation', 'date_of_employment', '  position']
