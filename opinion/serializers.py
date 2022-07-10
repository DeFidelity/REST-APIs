from rest_framework import serializers
from .models import Drop, Vote

class DropSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='drop.author')
    class Meta:
        model = Drop
        fields = ['id', 'title','author','body','created']
        
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']        
