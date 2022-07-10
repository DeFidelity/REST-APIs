from rest_framework import generics
from .models import Drop
from .serializers import DropSerializer

class DropListView(generics.ListAPIView):
    queryset = Drop.objects.all()
    serializer_class = DropSerializer
    
