import streamlit as st
import pickle
import json
import random
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# --- PREPROCESSING SETUP
factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()
factory_stop = StopWordRemoverFactory()
stopword_remover = factory_stop.create_stop_word_remover()

def text_preprocessing(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = stopword_remover.remove(text)
    text = stemmer.stem(text)
    return text

# --- LOAD RESOURCES ---
@st.cache_resource
def load_resources():
    # Load Model
    with open('models/chatbot_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Load Dataset JSON
    with open('data/dataset.json', 'r') as json_file:
        intents = json.load(json_file)
        
    return model, intents

model, intents_data = load_resources()

# --- LOGIC CHATBOT ---
def get_response(predicted_tag, intents_json):
    for intent in intents_json['intents']:
        if intent['tag'] == predicted_tag:
            # Mengambil satu jawaban acak dari list responses
            return random.choice(intent['responses'])
    return "Maaf, saya tidak mengerti."

# --- TAMPILAN UI ---
st.set_page_config(page_title="Virtual Assistant PMB", page_icon="🎓")

st.title("🎓 Asisten PMB Kampus")
st.markdown("---")
st.info("Hallo! aku Minci, Virtual Assistant PMB. Silakan tanyakan informasi seputar Pendaftaran Mahasiswa Baru ke Minci ya!")

# Session State untuk Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input User
if prompt := st.chat_input("Ketik pertanyaan kamu di sini ya!..."):
    # 1. Tampilkan Input User
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Proses Prediksi
    clean_input = text_preprocessing(prompt)
    prediction = model.predict([clean_input])[0]
    
    # Cek confidence level (opsional)
    probs = model.predict_proba([clean_input])
    confidence = probs.max()

    if confidence > 0.35: # Threshold
        response_text = get_response(prediction, intents_data)
    else:
        response_text = "Maaf, pertanyaan kamu kurang jelas nih. Bisa diulangi dengan kata lain ya kak!"

    # 3. Tampilkan Output Bot
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)