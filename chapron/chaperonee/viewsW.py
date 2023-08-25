# from .sum import perform_conversation_summarization,api_summary
# from django.http import HttpResponse,JsonResponse
# from .sentiment import api_sentiment,api_offensive
# from .medical import filtered, generate_topic_wordcloud
# from django.views.decorators.csrf import csrf_exempt
# from pymongo import MongoClient
# import openai, re
# import threading
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import chaperonee.config
# openai.api_key = chaperonee.config.api_key #chaperon key
# client = MongoClient(chaperonee.config.db)
# db = client['transcriptions']
# collection = db['transcriptions']
# from chaperonee.whisper_mic.whisper_mic import WhisperMic



# def save_transcription(transcription):

#             collection.insert_one({'transcription': transcription})
# def save_info(transcription,summary,sentiment, off_sentiment,terms):

#             collection.insert_one({'transcription': transcription,
#                                    'summary': summary,
#                                    'sentiment': sentiment,
#                                    'off_sentiment': off_sentiment,
#                                    'medical_term': terms})

# def ASR_WHISPER(mic):
#      result = mic.listen()
#      print("u say:" + result)
#      return result
   


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
#     mic = WhisperMic(english=True)


#     while not terminate_transcription:
#         try:
#                 text = ASR_WHISPER(mic)
#                 filtered_words.extend([word for word in specific_words if word in text and word not in filtered_words])
#                 for word in filtered_words:
#                  regex_pattern = r"\b" + re.escape(word) + r"s?\b"  # Match both singular and plural forms
#                  text = re.sub(regex_pattern, f"{word} (medical)", text)
#                  transcription.append(text)
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

