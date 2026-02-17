# Generated from: Friends (2).ipynb
# Converted at: 2026-02-16T19:11:29.790Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import numpy as np
import pandas as pd




import gensim
import os

with open("Friends_Transcript.txt","r") as f:
    corpus=f.read()

corpus


from nltk import word_tokenize
raw_sent=word_tokenize(corpus)

raw_sent



import string
translator = str.maketrans('', '', string.punctuation)
clean_text = [sent.translate(translator) for sent in raw_sent]

clean_text

lower_text=[word.lower() for word in clean_text]

from nltk.corpus import stopwords

sett=stopwords.words('english')

def remove_stopwords(text):
    new_text = []
    
    for word in text:
        if word not in sett:
            new_text.append(word)
            
    return new_text

    
   
    
    

    

new_story=remove_stopwords(lower_text)

new_story

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')




from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemmas = [lemmatizer.lemmatize(word) for word in new_story]





lemmas

# Step 2 — Train embeddings
from gensim.models import Word2Vec

model = Word2Vec([lemmas], min_count=1)

# Step 3 — Query


x=input()
model.wv.most_similar(x.lower())

