import json
import pandas as pd
import nltk
import pickle
import os
import re

# Library NLP Bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Scikit-Learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# --- 1. PREPROCESSING INITIALIZATION ---
factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()
factory_stop = StopWordRemoverFactory()
stopword_remover = factory_stop.create_stop_word_remover()

def text_preprocessing(text):
    # Lowercasing
    text = text.lower()
    # Cleaning (Hapus angka/simbol)
    text = re.sub(r'[^a-z\s]', '', text)
    # Stopword Removal
    text = stopword_remover.remove(text)
    # Stemming
    text = stemmer.stem(text)
    return text

# --- LOAD DATA ---
dataset_path = 'data/dataset.json'
print(f"Loading dataset from {dataset_path}...")

with open(dataset_path, 'r') as f:
    data = json.load(f)

# Format JSON ke DataFrame
dataset = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        dataset.append((pattern, intent['tag']))

df = pd.DataFrame(dataset, columns=['text', 'intent'])
print(f"Total data loaded: {len(df)}")

# --- APPLY PREPROCESSING ---
print("Melakukan Text Preprocessing...")
df['clean_text'] = df['text'].apply(text_preprocessing)

# --- SPLIT DATA ---
X = df['clean_text']
y = df['intent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 2. FEATURE ENGINEERING & 3. MODELING ---
# Pipeline 1: Naive Bayes
pipeline_nb = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Pipeline 2: Random Forest
pipeline_rf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', RandomForestClassifier(n_estimators=100))
])

# Training
print("\nSedang melatih Model 1 (Naive Bayes)...")
pipeline_nb.fit(X_train, y_train)

print("Sedang melatih Model 2 (Random Forest)...")
pipeline_rf.fit(X_train, y_train)

# --- 4. EVALUATION (TAMPILKAN KEDUANYA) ---
print("\n" + "="*40)
print("HASIL EVALUASI MODEL")
print("="*40)

# Evaluasi Naive Bayes
pred_nb = pipeline_nb.predict(X_test)
acc_nb = accuracy_score(y_test, pred_nb)
print(f"\n[MODEL 1] NAIVE BAYES (Akurasi: {acc_nb:.4f})")
print("-" * 40)
print(classification_report(y_test, pred_nb))

# Evaluasi Random Forest
pred_rf = pipeline_rf.predict(X_test)
acc_rf = accuracy_score(y_test, pred_rf)
print(f"\n[MODEL 2] RANDOM FOREST (Akurasi: {acc_rf:.4f})")
print("-" * 40)
print(classification_report(y_test, pred_rf))

# --- 5. SAVING MODEL ---
# Memilih model terbaik untuk disimpan
os.makedirs('models', exist_ok=True)
filename = 'models/chatbot_model.pkl'

if acc_nb >= acc_rf:
    best_model = pipeline_nb
    best_name = "Naive Bayes"
else:
    best_model = pipeline_rf
    best_name = "Random Forest"

pickle.dump(best_model, open(filename, 'wb'))

print("\n" + "="*50)
# Tampilan output diperbaiki sesuai permintaan
print(f"Model terbaik ({best_name}) berhasil disimpan ke '{filename}'")
print("="*50)