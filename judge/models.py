from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class ProblemFile(models.Model):
    prob_name = models.CharField(max_length=300)
    prob_desc = models.TextField()
    solution_file = models.FileField(upload_to='solutions/', max_length=400)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.prob_name)

    # Just to get a default value
    def get_default_problem():
        return ProblemFile.objects.first()

class Submission(models.Model):
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    prob_name = models.ForeignKey(ProblemFile, on_delete=models.CASCADE
                                  )
    submission_file = models.FileField(upload_to='submissions/', max_length=400)
    status = models.CharField(max_length=20, default='waiting')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.submitted_by} for Problem {self.prob_name}"

