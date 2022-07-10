from rest_framework import serializers
from .models import Drop

class DropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drop
        fields = ['id', 'title','author','body','created']
        