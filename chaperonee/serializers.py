from rest_framework import serializers
from chaperonee.models import  Conversation

class  ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Conversation
        fields=('_id', 'transcript_text','sum_text','created_at')