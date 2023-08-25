# from .sum import perform_conversation_summarization,api_summary
# from django.http import HttpResponse,JsonResponse
# from .sentiment import api_sentiment,api_offensive
# from .medical import filtered, generate_topic_wordcloud
# from django.views.decorators.csrf import csrf_exempt
# from pymongo import MongoClient
# import io,os
# import speech_recognition as sr
# from datetime import datetime, timedelta
# from queue import Queue
# from tempfile import NamedTemporaryFile
# import openai, re
# import sys 
# import threading
# from queue import Queue
# from datetime import datetime, timedelta
# import speech_recognition as sr
# from django.views.decorators.csrf import csrf_exempt
# from deepgram import Deepgram
# import asyncio
# dg_client = Deepgram("c2fd1e3216517d002f404f901d0e10190da53c56")
# from django.http import JsonResponse
# import chaperonee.config
# openai.api_key = chaperonee.config.api_key #chaperon key
# client = MongoClient(chaperonee.config.db)
# db = client['transcriptions']
# collection = db['transcriptions']
# import assemblyai as aai
# aai.settings.api_key = chaperonee.config.aai_key


# def save_transcription(transcription):

#             collection.insert_one({'transcription': transcription})
# def save_info(transcription,summary,sentiment, off_sentiment,terms):

#             collection.insert_one({'transcription': transcription,
#                                    'summary': summary,
#                                    'sentiment': sentiment,
#                                    'off_sentiment': off_sentiment,
#                                    'medical_term': terms})

# def ASR_WHISPER(payload):
#     file = open(payload, "rb")
#     response = openai.Audio.transcribe("whisper-1", file,target_language="fr")
#     return response["text"]


# specific_words = ['anatomie', 'pelvien', 'périnée', 'vagin', 'vaginal', 'anus', 'rectal',"rectum", "utérus", "utérin", "urètre", 
#                       "cavité", "endocavitaire" , "examens" , "vaginale", "mammaire","abdominal", "rectale", "échographie", "frottis",
#                       "prélèvement" , "instruments" ,"médicaux" , "speculum", "sondes", "gants", "lubrifiant", "pathologies" ,
#                       "HPV", "IST", "MST", "incontinence", "endométriose", "douleur" ,"périnéale"]

# # 
# @csrf_exempt
# def real_time_transcription(request):
#     global terminate_transcription, filtered_words, transcription

#     if request.method == 'POST':
#         threading.Thread(target=transcription_thread).start()  # Start the transcription in a separate thread

#     return JsonResponse({'message': 'Transcription started.'})

# def transcription_thread():
#     global terminate_transcription, filtered_words, transcription
#     terminate_transcription = False
#     filtered_words = []
#     transcription = [""]
#     phrase_time = None
#     last_sample = bytes()
#     data_queue = Queue()
#     recorder = sr.Recognizer()
#     recorder.energy_threshold = 250
#     recorder.dynamic_energy_threshold = False
#     source = sr.Microphone()
#     record_timeout = 5
#     phrase_timeout = 1
#     temp_file = NamedTemporaryFile(suffix=".wav").name

#     def record_callback(_, audio: sr.AudioData) -> None:
#         data = audio.get_raw_data()
#         data_queue.put(data)

#     recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)

#     while not terminate_transcription:
#         try:
#             now = datetime.utcnow()
#             if not data_queue.empty():
#                 phrase_complete = False
#                 if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
#                     last_sample = bytes()
#                     phrase_complete = True
#                 phrase_time = now
#                 while not data_queue.empty():
#                     data = data_queue.get()
#                     last_sample += data
#                 audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
#                 wav_data = io.BytesIO(audio_data.get_wav_data())
#                 with open(temp_file, 'w+b') as f:
#                     f.write(wav_data.read())
#                 text = ASR_WHISPER(temp_file)
#                 filtered_words.extend([word for word in specific_words if word in text and word not in filtered_words])
#                 if phrase_complete:
#                     for word in filtered_words:
#                         regex_pattern = r"\b" + re.escape(word) + r"s?\b"  # Match both singular and plural forms
#                         text = re.sub(regex_pattern, f"{word} (medical)", text)
#                     transcription.append(text)
#                 else:
#                     transcription[-1] = text
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 for line in transcription:
#                     print(line)
#                 print('', end='', flush=True)
#         except KeyboardInterrupt:
#             break
# def remove(text):
#         processed_text = re.sub(r'\(medical\)', '', text)
#         return processed_text

# @csrf_exempt
# def get_transcription(request):
#     global transcription, terminate_transcription

#     if request.method == 'GET':
#         terminate_transcription = True
#         transcription_text = "".join(transcription)
#         processed_text=remove(transcription_text)
#         print(processed_text)
#         summary=api_summary(transcription_text)
#         sentiment_results = api_sentiment(processed_text)
#         offensive_results = api_offensive(processed_text)
#         filtered_word=filtered(processed_text)
#         save_info(processed_text,summary,sentiment_results, offensive_results,filtered_word)
#         return JsonResponse({'transcription_text': transcription_text,
#                             'summary': processed_text,
#                             'sentiment_results': sentiment_results,
#                             'offensive_results': offensive_results,
#                             'medical_terms': filtered_word})

#     return JsonResponse({'message': 'Invalid request method.'})   

