from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch, json, requests
import numpy as np


# def api_sentiment(text):
#     headers = {
#         'Authorization': 'Bearer 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',
#         'Content-Type': 'application/json'}
#     data = {'inputs': text}
#     response = requests.post(
#         'https://axufh365p2m350u6.us-east-1.aws.endpoints.huggingface.cloud',
#         headers=headers,
#         data=json.dumps(data))
#     return response.json()

# def api_offensive(text):
#     headers = {
#         'Authorization': 'Bearer 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',
#         'Content-Type': 'application/json'}
#     data = {'inputs': text}
#     response = requests.post(
#         'https://opdcufiqw0i7diw7.eu-west-1.aws.endpoints.huggingface.cloud',
#         headers=headers,
#         data=json.dumps(data))
#     return response.json()

# def analyze_sentiment(text):
#     sentiment_tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-emotion")
#     sentiment_model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-emotion")

#     sentiment_inputs = sentiment_tokenizer(text, return_tensors="pt")
#     with torch.no_grad():
#         sentiment_logits = sentiment_model(**sentiment_inputs).logits

#     sentiment_results = {sentiment_model.config.id2label[i]: float(j) for i, j in enumerate(np.array(sentiment_logits[0]))}

#     return sentiment_results

# def detect_offensiveness(text):
#     offensive_tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
#     offensive_model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")

#     offensive_inputs = offensive_tokenizer(text, return_tensors="pt")
#     with torch.no_grad():
#         offensive_logits = offensive_model(**offensive_inputs).logits

#     offensive_results = {offensive_model.config.id2label[i]: float(j) for i, j in enumerate(np.array(offensive_logits[0]))}

#     return offensive_results


API_URL_em = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion"
headers = {"Authorization": "Bearer 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"}
def api_sentiment(payload):
	response = requests.post(API_URL_em, headers=headers, json=payload)
	return response.json()

API_URL_off = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-offensive"
headers = {"Authorization": "Bearer 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"}
def api_offensive(payload):
	response = requests.post(API_URL_off, headers=headers, json=payload)
	return response.json()





	
