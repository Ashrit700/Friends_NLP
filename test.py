# ==============================
# FRIENDS NLP – STREAMLIT APP
# Word2Vec Similarity Explorer
# ==============================

import streamlit as st
import numpy as np
import pandas as pd
import gensim
import nltk
import string
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ------------------------------
# Download NLTK resources
# ------------------------------
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# ------------------------------
# Title
# ------------------------------
st.title("📺 Friends Transcript NLP Explorer")
st.write("Find semantically similar words using Word2Vec embeddings.")

# ------------------------------
# Load transcript
# ------------------------------
@st.cache_data
def load_corpus():
    with open("Friends_Transcript.txt", "r", encoding="utf-8") as f:
        return f.read()

corpus = load_corpus()

# ------------------------------
# Preprocessing
# ------------------------------
@st.cache_data
def preprocess_text(corpus):

    # Tokenize
    tokens = word_tokenize(corpus)

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_text = [word.translate(translator) for word in tokens]

    # Lowercase
    lower_text = [word.lower() for word in clean_text]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in lower_text if w not in stop_words and w != ""]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in filtered_words]

    return lemmas

lemmas = preprocess_text(corpus)

# ------------------------------
# Train Word2Vec
# ------------------------------
@st.cache_resource
def train_model(lemmas):
    model = Word2Vec([lemmas], vector_size=100, window=5, min_count=1, workers=4)
    return model

model = train_model(lemmas)

# ------------------------------
# User Input
# ------------------------------
st.subheader("🔍 Word Similarity Search")

user_word = st.text_input("Enter a word:")

if user_word:

    try:
        results = model.wv.most_similar(user_word.lower())

        st.write("### Most Similar Words")

        df = pd.DataFrame(results, columns=["Word", "Similarity"])
        st.dataframe(df)

    except KeyError:
        st.error("Word not in vocabulary. Try another word.")