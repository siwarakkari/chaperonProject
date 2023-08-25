from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from django.http import HttpResponse
import requests, openai, json




# def perform_conversation_summarization(text):
#     tokenizer = AutoTokenizer.from_pretrained("kabita-choudhary/finetuned-bart-for-conversation-summary")
#     model = AutoModelForSeq2SeqLM.from_pretrained("kabita-choudhary/finetuned-bart-for-conversation-summary")

#     encoded_text = tokenizer(text, return_tensors="pt")
#     summary_ids = model.generate(**encoded_text)
#     summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
#     return summary

API_URL = "https://api-inference.huggingface.co/models/kabita-choudhary/finetuned-bart-for-conversation-summary"
headers = {"Authorization": "Bearer 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"}
def api_summary(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


# def api_summary(text):
#     headers = {
#         'Authorization': 'Bearer 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',
#         'Content-Type': 'application/json'}
#     data = {'inputs': text}
#     response = requests.post(
#         'https://nj2m45ve5zml3l2s.eu-west-1.aws.endpoints.huggingface.cloud',
#         headers=headers,
#         data=json.dumps(data))
#     return response.json()





# def transcribe_audio(path, model_size):
#     model = whisper.load_model(model_size)
#     result = model.transcribe(path)
#     segments = result["segments"]
#     text = result["text"]
#     return segments, text