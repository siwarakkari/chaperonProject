# from django.db import models
# from djongo.models.fields import ObjectIdField



# class Transcription(models.Model):
#     patientId = models.ForeignKey('Patient', on_delete=models.CASCADE)
#     roomId = models.CharField(max_length=255, default="")
#     transcription = models.TextField()
#     summary = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'transcriptions'  # Remplacez 'votre_collection_mongodb' par le nom réel de votre collection MongoDB
