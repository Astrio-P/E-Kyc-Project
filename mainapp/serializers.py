from rest_framework import serializers 
from .models import Customer, Student, Financial, Result, Course

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class academicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'