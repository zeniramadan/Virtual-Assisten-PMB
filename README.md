# 🎓 Virtual Assistant PMB

<!-- Tech Stack Shields -->
<p align="center">
   <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python"/>
   </a>
   <a href="https://streamlit.io/">
      <img src="https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit" alt="Streamlit"/>
   </a>
   <a href="https://scikit-learn.org/">
      <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn" alt="Scikit-learn"/>
   </a>
   <a href="https://github.com/har07/Sastrawi">
      <img src="https://img.shields.io/badge/Sastrawi-NLP-green" alt="Sastrawi"/>
   </a>
   <a href="https://www.nltk.org/">
      <img src="https://img.shields.io/badge/NLTK-NLP-yellow?logo=nltk" alt="NLTK"/>
   </a>
</p>

Virtual Assistant PMB (Minci) adalah chatbot cerdas berbasis Bahasa Indonesia yang membantu calon mahasiswa mendapatkan informasi seputar **Penerimaan Mahasiswa Baru (PMB)** secara otomatis, cepat, dan interaktif. Dibangun menggunakan Streamlit dan machine learning, Minci siap menjawab pertanyaan seputar biaya, syarat, jadwal, jurusan, lokasi, beasiswa, hingga kontak admin kampus!

---

## 🚀 Fitur Utama

- **Chatbot Interaktif**: Tanyakan apa saja seputar PMB, Minci akan menjawab secara real-time.
- **Natural Language Processing (NLP)**: Memahami bahasa sehari-hari calon mahasiswa.
- **Data Augmentation**: Variasi pertanyaan diperbanyak secara otomatis agar model lebih pintar.
- **Akurat & Informatif**: Jawaban diambil dari dataset dan model yang sudah dilatih khusus PMB.

## 🛠️ Teknologi yang Digunakan

### Tech Stack

- Python 3.10+
- Streamlit (UI Chatbot)
- Scikit-learn (Machine Learning)
- Sastrawi (NLP Bahasa Indonesia)
- NLTK

## 📦 Instalasi & Menjalankan

1. **Clone repository ini**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Generate dataset (opsional, jika ingin memperbarui data):**
   ```bash
   python generate_data.py
   ```
4. **Latih model:**
   ```bash
   python train_model.py
   ```
5. **Jalankan aplikasi chatbot:**
   ```bash
   streamlit run app.py
   ```

## 💬 Contoh Pertanyaan

- "Berapa biaya daftar?"
- "Apa saja syarat pendaftaran?"
- "Kapan pendaftaran dibuka?"
- "Ada beasiswa nggak?"
- "Nomor WA admin berapa?"

## 📁 Struktur Folder

```bash
Virtual-Assisten-PMB/
├── data/
│   └── dataset.json      # Dataset intent & response
├── models/
│   └── chatbot_model.pkl # Model hasil training
├── app.py                # Streamlit chatbot utama
├── generate_data.py      # Script pembuatan/augmentasi dataset
├── train_model.py        # Script pelatihan & evaluasi model
├── requirements.txt      # Daftar dependencies
└── README.md             # Dokumentasi

```

---

**Dikembangkan oleh Tim NLP Kelompok 2**

> STT Cipasung, 2025
