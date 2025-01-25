from django.urls import path,include
from .views import  CreateProblemAPIView, CreateSubmissionAPIView

urlpatterns = [path('create-problem/', CreateProblemAPIView.as_view(), name='create-problem'),
path('submissions/', CreateSubmissionAPIView.as_view(), name='submissions'),   
]
