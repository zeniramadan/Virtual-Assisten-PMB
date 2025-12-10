# 🎓 Virtual Assistant PMB

Virtual Assistant PMB (Minci) adalah chatbot cerdas berbasis Bahasa Indonesia yang membantu calon mahasiswa mendapatkan informasi seputar **Penerimaan Mahasiswa Baru (PMB)** secara otomatis, cepat, dan interaktif. Dibangun menggunakan Streamlit dan machine learning, Minci siap menjawab pertanyaan seputar biaya, syarat, jadwal, jurusan, lokasi, beasiswa, hingga kontak admin kampus!

---

## 🚀 Fitur Utama

- **Chatbot Interaktif**: Tanyakan apa saja seputar PMB, Minci akan menjawab secara real-time.
- **Natural Language Processing (NLP)**: Memahami bahasa sehari-hari calon mahasiswa.
- **Data Augmentation**: Variasi pertanyaan diperbanyak secara otomatis agar model lebih pintar.
- **Akurat & Informatif**: Jawaban diambil dari dataset dan model yang sudah dilatih khusus PMB.

## 🛠️ Teknologi yang Digunakan

- Python 3
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

- `app.py` : Aplikasi utama chatbot
- `generate_data.py` : Script untuk membuat/augmentasi dataset
- `train_model.py` : Script pelatihan model ML
- `data/dataset.json` : Dataset intent & response
- `models/` : Model hasil training

---

**Dikembangkan oleh Tim NLP Kelompok 2**

> STT Cipasung, 2025
