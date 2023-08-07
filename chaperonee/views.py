from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chaperonproject.whisper_mic.whisper_mic import WhisperMic
from django.views.decorators.csrf import csrf_exempt
import keyboard 
from chaperonproject.test import summarization
from rest_framework.parsers import JSONParser
from chaperonproject.models import Conversation
from chaperonproject.serializers import ConversationSerializer
from chaperonproject.emotion import process
import re
from chaperonproject.medical import filtered,remove



# specific_words = ['anatomie', 'pelvien', 'périnée', 'vagin', 'vaginal', 'anus', 'rectal',"rectum", "utérus", "utérin", "urètre", 
#                       "cavité", "endocavitaire" , "examens" , "vaginale", "mammaire","abdominal", "rectale", "échographie", "frottis",
#                       "prélèvement" , "instruments" ,"médicaux" , "speculum", "sondes", "gants", "lubrifiant", "pathologies" ,
#                       "HPV","muscles," "IST", "MST", "incontinence", "endométriose", "douleur" ,"périnéale","testing","examination","pressure"]
@csrf_exempt
def transcribe(request):
  if request.method == 'POST':
    #  global  filtered_words
    #  filtered_words = []
     res=""
     i=0
     mic = WhisperMic(english=True)
     while i<5 :
       result = mic.listen()
       print("You said: " + result)
      #  processed_text=remove(result)
      #  filtered_word=filtered(processed_text)
       res += result +" "
       i+=1

      #  filtered_words.extend([word for word in specific_words if word in result and word not in filtered_words])
      #  for word in filtered_words:
      #      regex_pattern = r"\b" + re.escape(word) + r"s?\b"  # Match both singular and plural forms
      #      result = re.sub(regex_pattern, f"{word} (medical)", result)
      #  print(filtered_word)
      #  process(result)
     print(res)
     rrr=summarization(res)
     conversation = Conversation(transcript_text=res)
     conversation = Conversation(sum_text=rrr)
     conversation.save()



  elif request.method =='GET':
     stor=Conversation.objects.all()
     stor_serializer=ConversationSerializer(stor,many=True)
     return JsonResponse(stor_serializer.data, safe=False)
