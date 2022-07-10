from django.urls import path 
from .views import DropListView,VoteCreateView


urlpatterns = [ 
    path('all/',DropListView.as_view(), name='drop'),     
    path('<int:pk>/vote/',VoteCreateView.as_view(), name='vote')       
]