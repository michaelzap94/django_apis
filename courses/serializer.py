from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course object"""

    class Meta:
        model = Course
        fields = ('id', 'name', 'language', 'price')
        read_only_Fields = ('id',)
