from django.urls import path 
from .views import DropListView


urlpatterns = [ 
    path('all/',DropListView.as_view(), name='drop'),            
               ]