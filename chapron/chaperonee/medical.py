from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from tqdm import tqdm
import string
import nltk
import regex as re
import warnings
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')


stemmer = SnowballStemmer(language="english")
lemmatizer = WordNetLemmatizer()
punct = '!"#$%&\'()*+-/<=>?@[\]^`{|}~'
stop_words = set(stopwords.words('french'))
punctuation = string.punctuation

def remove(text):
        processed_text = re.sub(r'\(medical\)', '', text)
        return processed_text
def process_text(s):
    for p in punct:
        s = s.replace(p, '')
    s = word_tokenize(s)
    s = [w for w in s if not w in stop_words]
    return s

def generate_wordcloud(i, ranked_words):
    ranked_words_in_one_text = " ".join(ranked_words)
    cloud = WordCloud(background_color='black', colormap="viridis").generate(ranked_words_in_one_text)
    words = cloud.words_
    sorted_words = sorted(words, key=words.get, reverse=True)
    word_string = ", ".join(sorted_words)
    print(f"Words in word cloud for subject {i}: {word_string}")
    plt.figure(figsize=(10, 8))
    plt.imshow(cloud)
    plt.title("Most common words")
    plt.axis("off")
    plt.show()

def generate_topic_wordcloud(text):
    processed_text = process_text(text)
    processed_text = " ".join(processed_text)

    vectorizer = TfidfVectorizer()
    texts = [processed_text]
    tfidf_data = vectorizer.fit_transform(texts).toarray()
    tfidf_features = vectorizer.get_feature_names_out()
    tfidf_data = pd.DataFrame(tfidf_data, columns=tfidf_features)

    lda = LatentDirichletAllocation(n_components=1)
    mat = lda.fit_transform(tfidf_data)

    topic_word = lda.components_

    number_of_topics = topic_word.shape[0]
    for i in range(number_of_topics):
        words_dist = topic_word[i, :]
        ranked_word_indices = words_dist.argsort()
        ranked_words = [tfidf_features[i] for i in ranked_word_indices][-1:-40:-1]
        generate_wordcloud(i, ranked_words)

def filtered(text):
    processed_text = process_text(text)
    processed_text = " ".join(processed_text)

    if not processed_text:
        return []  # Return an empty list if the processed text is empty

    vectorizer = TfidfVectorizer()
    texts = [processed_text]
    tfidf_data = vectorizer.fit_transform(texts).toarray()
    tfidf_features = vectorizer.get_feature_names_out()
    tfidf_data = pd.DataFrame(tfidf_data, columns=tfidf_features)

    lda = LatentDirichletAllocation(n_components=1)
    mat = lda.fit_transform(tfidf_data)

    topic_word = lda.components_

    number_of_topics = topic_word.shape[0]
    result = []
    for i in range(number_of_topics):
        words_dist = topic_word[i, :]
        ranked_word_indices = words_dist.argsort()
        ranked_words = [tfidf_features[i] for i in ranked_word_indices][-1:-40:-1]
        result += ranked_words

    # Filter specific words
    specific_words = ['anatomie', 'pelvien', 'périnée', 'vagin', 'vaginal', 'anus', 'rectal',"rectum", "utérus", "utérin", "urètre", 
                      "cavité", "endocavitaire" , "examens" , "vaginale", "mammaire","abdominal", "rectale", "échographie", "frottis",
                      "prélèvement" , "instruments" ,"médicaux" , "speculum", "sondes", "gants", "lubrifiant", "pathologies" ,
                      "HPV","muscles," "IST", "MST", "incontinence", "endométriose", "douleur" ,"périnéale","testing","examination","pressure"]

    detected_medical_words = []
    for word in specific_words:
        regex_pattern = r"\b" + re.escape(word) + r"s?\b"  # Match both singular and plural forms
        if re.search(regex_pattern, processed_text):
            detected_medical_words.append(word)

    return detected_medical_words