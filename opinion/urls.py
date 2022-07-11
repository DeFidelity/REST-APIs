from django.urls import path 
from .views import DropListView,VoteCreateView,DropDeleteAndRetrieve


urlpatterns = [ 
    path('all/',DropListView.as_view(), name='drop'),     
    path('<int:pk>/vote/',VoteCreateView.as_view(), name='vote'),
    path('<int:pk>/retdel/',DropDeleteAndRetrieve.as_view(),name='retdel')  
]