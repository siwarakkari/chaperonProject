import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from chaperonee.whisper_mic.whisper_mic import WhisperMic
from django.views.decorators.csrf import csrf_exempt
from chaperonee.test import summarization
from rest_framework.parsers import JSONParser
from pymongo import MongoClient
from djongo.models.fields import ObjectId

 

def get_transcription_summary(request):
    try:
        client = MongoClient('mongodb+srv://siwarbouzidi:UXQXwYW1cB5hnjch@cluster0.kualaf6.mongodb.net/') # Replace with your MongoDB URI
        db = client['test']
        collection = db['transcriptions']
        cursor = collection.find({})
        print(cursor)
        print(type (cursor))
        documents = [document for document in cursor]
        print(type ( documents))
        return HttpResponse(documents)

        # # data = []
        # for transcription in transcriptions:
        #     data.append({
        #         'roomId': transcription['roomId'],
        #         'transcription': transcription['transcription'],
        #         'summary': transcription['summary'],
        #         'created_at': transcription['created_at'],
        #     })

        # return JsonResponse({'data': data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
  
  
 


