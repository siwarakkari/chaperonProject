from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

def process(text):
    
    
# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

  task='emotion'
  MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

  tokenizer = AutoTokenizer.from_pretrained(MODEL)

# download label mapping
  labels=[]
  mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
  with urllib.request.urlopen(mapping_link) as f:
      html = f.read().decode('utf-8').split("\n")
      csvreader = csv.reader(html, delimiter='\t')
  labels = [row[1] for row in csvreader if len(row) > 1]


# PT
  model = AutoModelForSequenceClassification.from_pretrained(MODEL)
  model.save_pretrained(MODEL)
  tokenizer.save_pretrained(MODEL)


  encoded_input = tokenizer(text, return_tensors='pt')
  output = model(**encoded_input)
  scores = output[0][0].detach().numpy()
  scores = softmax(scores)


  ranking = np.argsort(scores)
  ranking = ranking[::-1]
  for i in range(scores.shape[0]):
      l = labels[ranking[i]]
      s = scores[ranking[i]]
      
      print(f"{i+1}) {l} {np.round(float(s), 4)}")
      if ( labels[ranking[i]] == "anger" or labels[ranking[i]] == "sadness") and scores[ranking[i]] > 0.5000 :
         print ("is every thing is okay?")
         return("VIOLENCE DETECTED")
      else:
         return ("0")
         
   