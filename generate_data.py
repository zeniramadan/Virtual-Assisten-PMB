import json
import os
import random

# Definisi Intent Dasar
intents_template = [
    {
        "tag": "salam",
        "patterns": ["halo", "hai", "selamat pagi", "selamat siang", "ping", "permisi", "min", "hallo admin", "assalamua'alaikum"],
        "responses": ["Halo kak! Ada yang bisa Minci bantu terkait PMB?", "Hai calon mahasiswa! Silakan tanya seputar pendaftaran ke Minci ya!.", " Halo kak, selamat datang di layanan informasi PMB. Silahkan tanya ke Minci ya!"]
    },
    {
        "tag": "biaya_pendaftaran",
        "patterns": ["berapa biaya daftar?", "harganya berapa?", "bayar formulir berapa", "biaya pendaftaran mahasiswa baru", "biaya masuk berapa", "uang pendaftaran", "transfer berapa"],
        "responses": ["Biaya pendaftarannya Rp 250.000 saja ya kak.", "Untuk pendaftaran dikenakan biaya Rp 250.000 saja ya kak.", "Cukup membayar Rp 250.000 untuk biaya pendaftarannya ya kak."]
    },
    {
        "tag": "syarat_pendaftaran",
        "patterns": ["apa saja syaratnya?", "dokumen apa yang dibutuhkan?", "syarat daftar", "berkas pendaftaran", "ketentuan pendaftaran", "butuh ijazah apa?", "persyaratan maba"],
        "responses": ["Syaratnya kakak Scan atau fotokopi Ijazah/SKL, KTP, KK, dan Pas Foto terbaru ya!.", "Kakak hanya perlu menyiapkan Fotokopi Ijazah legalisir, KTP, KK, dan Foto berwarna.", "Dokumen wajibnya Fotokopi Ijazah, KTP, KK, dan Pas Foto Berwarna saja kak."]
    },
    {
        "tag": "jadwal_pendaftaran",
        "patterns": ["kapan pendaftaran dibuka?", "tanggal berapa tutup?", "deadline pendaftaran", "jadwal gelombang 1", "jadwal gelombang 2", "kapan terakhir daftar?", "kalender pendaftaran"],
        "responses": ["Gelombang 1 itu 20 Januari-20 Maret 2026 dan untuk Gelombang 2 itu 20 April - 20 Juni 2026. Pendaftarannya dibuka setiap hari kerja hingga bulan Agustus."]
    },
    {
        "tag": "jurusan_prodi",
        "patterns": ["ada jurusan apa aja?", "prodi yang tersedia", "fakultas apa saja?", "list jurusan", "pilihan prodi", "teknik informatika ada gak?", "program studi"],
        "responses": ["Kami memiliki program studi Teknik Informatika dan Teknik Industri kak."]
    },
    {
        "tag": "lokasi_kampus",
        "patterns": ["lokasi kampus dimana?", "alamat kampus", "kampusnya dimana?", "share loc kampus", "tempat kuliah", "gedung kampus"],
        "responses": ["Kampus STT Cipasung berlokasi di Jl. Cisinga No.KM1, Cilampunghilir, Kec. Padakembang, Kabupaten Tasikmalaya, Jawa Barat 46466.", "Lokasi kami ada di Kabupaten Tasikmalaya, dekat pesantren Cipasung, tepatnya di Jl. Cisinga No.KM1, Cilampunghilir, Kec. Padakembang, Kabupaten Tasikmalaya, Jawa Barat 46466.", "Alamat lengkapnya di Jl. Cisinga No.KM1, Cilampunghilir, Kec. Padakembang, Kabupaten Tasikmalaya, Jawa Barat 46466."]
    },
    {
        "tag": "kontak_admin",
        "patterns": ["bisa hubungi siapa?", "nomor wa admin", "call center", "email kampus", "kontak person", "nomor telepon"],
        "responses": ["Hubungi WhatsApp Minci ya di 0812-3456-7890, Email ke pmb@sttcipasung.ac.id, dan Layanan telepon juga tersedia di (021) 555-555."]
    },
    {
        "tag": "beasiswa",
        "patterns": ["ada beasiswa gak?", "program beasiswa", "potongan", "beasiswa kip", "daftar beasiswa", "diskon uang gedung"],
        "responses": ["Minci kasih tau nih kak, di kampus STT Cipasung tersedia beasiswa KIP-K dan Beasiswa Prestasi. Ada juga potongan 50% uang gedung untuk ranking 1-3 di sekolah, dan Kami juga menyediakan jalur beasiswa yayasan sebesar 100%, 70%, dan 50% kak."]
    },
    {
        "tag": "penutup",
        "patterns": ["terima kasih", "makasih min", "thanks", "oke makasih infonya", "baik terima kasih", "cukup jelas, makasih", "sampai jumpa", "dadah", "tengkyu"],
        "responses": ["Sama-sama kak! Minci do'akan semoga sukses pendaftarannya ya.", "Terima kasih kembali kak. Jika ada pertanyaan lain, jangan ragu untuk menghubungi Mici lagi ya!.", "Senang bisa membantu! Minci tunggu kedatangannya menjadi bagian dari mahasiswa baru kami."]
    }
]

def generate_dataset():
    final_intents = []
    total_patterns = 0
    
    # Kata tambahan untuk memperbanyak variasi data
    prefixes = ["tolong infokan", "mau tanya", "min", "pak/bu", "kalo", "info dong", "jelaskan tentang", "mohon info"]
    suffixes = ["gimana ya?", "terima kasih", "please", "cepetan", "ya", "dong", "thanks", "segera"]

    for intent in intents_template:
        augmented_patterns = list(intent["patterns"])
        
        # Data Augmentation: Kombinasi kata
        for base in intent["patterns"]:
            for pre in prefixes:
                augmented_patterns.append(f"{pre} {base}")
            for suf in suffixes:
                augmented_patterns.append(f"{base} {suf}")
        
        intent["patterns"] = list(set(augmented_patterns)) # Hapus duplikat
        total_patterns += len(intent["patterns"])
        final_intents.append(intent)

    data = {"intents": final_intents}
    
    # Membuat folder data jika belum ada
    os.makedirs('data', exist_ok=True)
    
    # Simpan ke data/dataset.json
    output_path = 'data/dataset.json'
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Sukses! Dataset dengan {total_patterns} data tersimpan di '{output_path}'")

if __name__ == "__main__":
    generate_dataset()