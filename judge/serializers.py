from rest_framework import serializers
from .models import   ProblemFile,Submission


from rest_framework import serializers
from .models import ProblemFile

from rest_framework import serializers
from .models import ProblemFile

class ProblemFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemFile
        fields = ['id', 'prob_name', 'prob_desc', 'solution_file', 'created_by']
        read_only_fields = ['id', 'created_by']

    def create(self, validated_data):
        # Ensure 'created_by' is set from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user

        # Create and return the ProblemFile instance
        return ProblemFile.objects.create(**validated_data)


class CreateSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['submitted_by', 'prob_name', 'filename', 'submission_file', 'status', 'submitted_at']
        read_only_fields = ['id', 'status']

    def validate_submission_file(self, value):
        if value.size > 5 * 1024 * 1024:  # 5MB size limit
            raise serializers.ValidationError("Submission file size must be less than 5MB.")
        return value
