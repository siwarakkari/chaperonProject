from rest_framework import serializers
from chaperonee.models import  Transcription

class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Transcription
        fields=('patientId', ' roomId','transcription','summary','created_at')