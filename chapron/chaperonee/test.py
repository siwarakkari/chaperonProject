from summarizer import Summarizer
from transformers import logging


def summarization(text):
    
    bert_model = Summarizer()
    bert_summary = ''.join(bert_model(text, min_length=30))
    logging.set_verbosity_warning()
    print(bert_summary)
    return bert_summary
