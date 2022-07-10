from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Drop, Vote
from .serializers import DropSerializer, VoteSerializer
from django.shortcuts import get_object_or_404

class DropListView(generics.ListCreateAPIView):
    queryset = Drop.objects.all()
    serializer_class = DropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    
class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permissions = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        voter = self.request.user
        drop = Drop.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=voter,drop=drop)
    
    
    def perform_create(self,serializer):
        if self.get_queryset().exists():
            raise ValidationError("You've already voted this drop.")
        return serializer.save(voter=self.request.user,drop=Drop.objects.get(pk=self.kwargs['pk']))