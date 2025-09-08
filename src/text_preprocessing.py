import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


def preprocess_text(text, language='english'):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words(language))
    cleaned = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(cleaned)
