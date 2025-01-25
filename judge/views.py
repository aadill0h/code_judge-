from django.shortcuts import render
from rest_framework import generics
from .models import ProblemFile, Submission
from .serializers import  ProblemFileSerializer, CreateSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
#from .tasks import run_code
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
        submission= serializer.save(submitted_by=self.request.user)

        '''run_code.delay(
            submission_id=submission.id,
            script_filename=submission.filename.name,
            solution_filename=submission.prob_name + "_solution.txt")
'''