from rest_framework import serializers
from .models import Course # we need to serialize the model data

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course object"""

    #
    class Meta:
        model = Course # name of model
        fields = ('id', 'name', 'language', 'price') #fields we want to serialize( convert to/from JSON)
        read_only_Fields = ('id',) #fields that we want to protect
