from rest_framework import serializers
from chaperonproject.models import  Conversation

class  ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Conversation
        fields=('_id', 'transcript_text','sum_text','created_at')