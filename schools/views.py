from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student
from rest_framework import filters

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'max_num_of_students']
    ordering_fields = ['name', 'max_num_of_students']
    ordering = ['name']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # filterset_fields = ['first_name', 'last_name', 'student_id', 'school__name']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'student_id', 'school__name']
    ordering_fields = ['last_name', 'first_name', 'student_id', 'school__name']
    ordering = ['last_name']

    def get_queryset(self):
        if 'schools_pk' in self.kwargs:
            return Student.objects.filter(school=self.kwargs['schools_pk'])
        else:
            return Student.objects.all()

