from rest_framework import serializers 
from .models import Customer, Student, Financial, Result, Personal, Course

class personalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class academicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'