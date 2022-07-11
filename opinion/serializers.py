from rest_framework import serializers
from .models import Drop, Vote

class DropSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='drop.author')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Drop
        fields = ['id', 'title','author','body','created','votes']
        
    def get_votes(self, drop):
        return Vote.objects.filter(drop=drop).count()
        

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']        
        
   
