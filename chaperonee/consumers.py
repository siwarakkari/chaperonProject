from datetime import datetime
import json
from django.http import HttpResponse,JsonResponse
from .sentiment import api_sentiment,api_offensive
from .medical import filtered, generate_topic_wordcloud
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import openai, re
import threading
import chaperonee.config
from chaperonee.whisper_mic.whisper_mic import WhisperMic
from chaperonee.whisper_mic.whisper_mic import WhisperMic
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from chaperonee.emotion import process
from .sum import api_summary


openai.api_key = chaperonee.config.api_key #chaperon key
client = MongoClient(chaperonee.config.db)
db = client['test']
collection = db['transcriptions']


class Transcription(WebsocketConsumer):
   global terminate_transcription
   global patientId
   transcription = ""
   global summary,roomId
   specific_words = ['pressures','pressure','vagina','lubricant','bladder','Cytron machine','test','testing','catheter','laser','treatment','vaginal canal','clinic','anatomie', 'pelvien', 'périnée', 'vagin', 'vaginal', 'anus', 'rectal',"rectum", "utérus", "utérin", "urètre", 
                      "cavité", "endocavitaire" , "examens" , "vaginale", "mammaire","abdominal", "rectale", "échographie", "frottis",
                      "prélèvement" , "instruments" ,"médicaux" , "speculum", "sondes", "gants", "lubrifiant", "pathologies" ,
                      "HPV", "IST", "MST", "incontinence", "endométriose", "douleur" ,"périnéale"]

   def connect(self):
        self.accept()
        print('connected')
        threading.Thread(target=self.transcription_thread).start()  # Start the transcription in a separate thread

   def ASR_WHISPER(self,mic):
     result = mic.listen()
     print(result)
   #   self.send(text_data=result)
     return result
   
   def transcription_thread(self):
      global filtered_words
    
      self.terminate_transcription = False
      filtered_words = []
    
      mic = WhisperMic(english=True)


      while not self.terminate_transcription:
        try:
                x=""
                text = self.ASR_WHISPER(mic)
                filtered_words.extend([word for word in self.specific_words if word in text and word not in filtered_words])
                for word in filtered_words:
                 regex_pattern = r"\b" + re.escape(word) + r"s?\b"  # Match both singular and plural forms
                 text = re.sub(regex_pattern, f"{word} (medical)", text)

                self.transcription=self.transcription+text
                self.send(text_data=text)
                x=process(text)
                if x!= "0" :
                    self.send(f'violence: {x}' )
                    

        except KeyboardInterrupt:
            break
        

   def receive(self, text_data):
        try:
            data = json.loads(text_data)
            if 'user_id' in data:
                # Assuming 'user_id' is the key for the user ID in the received data
                patientId = data['user_id']
                roomId=data['roomid']
                # Now, you can use the 'patientId' variable as needed, e.g., storing it in a global variable
                self.patientId = patientId
                self.roomId=roomId
                print(f"Received user ID: {patientId} {roomId}")
        except json.JSONDecodeError:
            print("Invalid JSON format")






   def disconnect(self, close_code):
          print(self.transcription)
          self.summary=api_summary(self.transcription)
          print (self.summary)
          collection.insert_one ( {
                                   'patientId':self.patientId,
                                   'roomId':self.roomId,
                                   'transcription': self.transcription,
                                   'summary': self.summary,
                                   'createdAt': datetime.now(),
                                   'updatedAt': datetime.now(),
                                   '__v': 0,

                                  #  'sentiment': sentiment,
                                  #  'off_sentiment': off_sentiment,
                                  #  'medical_term': terms
                                   })
          self.close()
          self.terminate_transcription = True
        # Perform any cleanup or additional actions here
          print("WebSocket connection closed")
          raise StopConsumer()

          

                

   
    