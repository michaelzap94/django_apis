from django.shortcuts import render
from rest_framework import viewsets #sets of pages that the rest_framework will create for us
from .models import Course
from .serializer import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all() # this is the model (dataset), so we need to pull out the data
    serializer_class = CourseSerializer # Specify which serializer_class to use (show) when this view is accessed/served
    
