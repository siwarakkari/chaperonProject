from django.db import models
from djongo.models.fields import ObjectIdField

class Conversation(models.Model):
    _id = ObjectIdField(primary_key=True)  
    transcript_text = models.TextField()
    sum_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
