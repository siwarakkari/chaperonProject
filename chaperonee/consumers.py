import json
from channels.generic.websocket import WebsocketConsumer
from chaperonee.whisper_mic.whisper_mic import WhisperMic


class Transcription(WebsocketConsumer):
    def connect(self):
        print("hi")
        self.accept()
        print('cfonnected')

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'you are connected!'

        }))
        mic = WhisperMic(english=True)
        while True :
         res=""
         result = mic.listen()
         print("You said: " + result)
         res += result +" "
     #  processed_text=rem
         self.send(text_data=json.dumps({'message': result}))