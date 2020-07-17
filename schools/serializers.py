from rest_framework import serializers
from .models import School, Student

class SchoolSerializer(serializers.ModelSerializer):
    # current_num_of_students = serializers.integerField(read_only=True)

    class Meta:
        model = School
        fields = ['name', 'max_num_of_students']

class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'school', 'student_id']


