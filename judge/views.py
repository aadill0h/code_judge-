from django.shortcuts import render
from rest_framework import generics
from .models import ProblemFile, Submission
from .serializers import  ProblemFileSerializer, CreateSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CreateProblemAPIView(generics.CreateAPIView):
    queryset = ProblemFile
    serializer_class = ProblemFileSerializer
    permission_classes  = [IsAuthenticated]

    def perform_create(self, serialiser):
        serialiser.save( created_by= self.request.user)


class CreateSubmissionAPIView(generics.CreateAPIView):
    queryset = Submission
    serializer_class = CreateSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)
