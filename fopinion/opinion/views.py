from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
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


class DropDeleteAndRetrieve(generics.RetrieveDestroyAPIView):
    queryset = Drop.objects.all()
    serializer_class = DropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def delete(self,request, *args, **kwargs):
        drop = Drop.objects.filter(pk=kwargs['pk'],author=self.request.user)
        if drop:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("WYD Bro? You don't even own the post and you want to delete.")
class VoteCreateView(generics.CreateAPIView, mixins.DestroyModelMixin):
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
    
    def delete(self, serializer,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            raise ValidationError("You never support this opinion gee!")