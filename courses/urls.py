from django.urls import path, include
from . import views
from rest_framework import routers # allows us to create GET and POST requests

#1)create router
router = routers.DefaultRouter()
#2)register router
router.register('courses', views.CourseView) # 1st param -> url to access this view, 2nd param -> the view extending rest_framework viewsets.ModelViewSet


urlpatterns = [
    path('', include(router.urls)),
]