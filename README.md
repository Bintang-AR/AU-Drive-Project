# 🚗 AUDRIVE

### *Listen Early, Drive Safer*

**AUDRIVE (Automotive Diagnostic via Audio, Vibration & Telemetry)** adalah aplikasi diagnosis kondisi mesin kendaraan yang memanfaatkan **audio mesin, getaran, dan data telemetri** untuk membantu mendeteksi potensi kerusakan kendaraan sejak dini.

Sistem menggunakan **Deep Learning** untuk menganalisis karakteristik suara mesin dan menghasilkan informasi diagnosis berupa:

* 🔍 Jenis kerusakan
* ⚠️ Tingkat keparahan
* 🛠️ Rekomendasi tindakan
* 💰 Estimasi biaya servis

AUDRIVE dirancang untuk kendaraan seperti **sepeda motor, mobil, maupun kendaraan fleet**.

---

## 👥 Anggota Tim

| No. | Nama                        |
| :-: | --------------------------- |
|  1  | **Andika Bintang Ramadhan** |
|  2  | **Muhammad Iqbal**          |
|  3  | **Muhamad Ikhsan Ramadhan** |
|  4  | **Rasyiq Surya Ramadhan**   |

---

## 🎯 Latar Belakang

Kerusakan mesin kendaraan sering kali sulit dikenali oleh pemilik kendaraan sebelum masalah berkembang menjadi lebih serius.

Beberapa permasalahan yang menjadi dasar pengembangan AUDRIVE:

### 🔊 1. Sulit mengenali suara mesin abnormal

Pemilik kendaraan pada umumnya tidak memiliki pengetahuan atau pengalaman yang cukup untuk membedakan suara mesin normal dan suara yang mengindikasikan adanya kerusakan.

### 🔧 2. Diagnosis masih bergantung pada mekanik

Pemeriksaan kendaraan biasanya membutuhkan mekanik atau teknisi yang berpengalaman. Pada kendaraan tertentu, proses diagnosis juga membutuhkan perangkat khusus seperti **scanner kendaraan**.

### 💸 3. Biaya alat diagnosis relatif mahal

Perangkat diagnosis profesional tidak selalu terjangkau bagi pengguna umum, sehingga diperlukan alternatif diagnosis yang lebih mudah diakses.

### 📱 4. Belum banyak solusi diagnosis berbasis suara yang mudah digunakan

AUDRIVE dikembangkan sebagai pendekatan alternatif dengan memanfaatkan **audio mesin dan teknologi Machine Learning** sehingga proses pemeriksaan awal dapat dilakukan dengan lebih praktis.

---

## 💡 Solusi

AUDRIVE memanfaatkan data yang berasal dari kendaraan untuk melakukan proses analisis secara otomatis.

Secara umum, sistem bekerja dengan alur:

```text
┌─────────────────────┐
│   Kendaraan         │
│                     │
│  Audio + Getaran    │
│  + Telemetri        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Audio Processing    │
│ & Preprocessing     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Deep Learning Model │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Diagnosis        │
│                     │
│ • Jenis Kerusakan   │
│ • Severity          │
│ • Recommendation    │
│ • Estimasi Biaya    │
└─────────────────────┘
```

---

## 🧠 Teknologi yang Digunakan

### Machine Learning

* **Convolutional Neural Network (CNN)**
* **Convolutional Recurrent Neural Network (CRNN)**
* Deep Learning
* Model inference menggunakan TensorFlow/Keras

### Audio Processing

* Audio preprocessing
* Audio conversion
* Spectrogram
* Feature extraction
* Analisis karakteristik suara mesin

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* TensorFlow / Keras

### Frontend

* **Node.js**
* **TypeScript**
* **React**
* Web-based User Interface

### Development Environment

* Git / GitHub
* npm
* Python virtual environment
* FFmpeg

---

# 📁 Struktur Project

Struktur utama repository AUDRIVE:

```text
AU-Drive-Project/
│
├── node_modules/
│
└── src/
    │
    ├── audio/
    │
    ├── backend/
    │   │
    │   ├── __pycache__/
    │   │
    │   ├── audio/
    │   │   ├── convert.py
    │   │   └── preprocess.py
    │   │
    │   ├── models/
    │   │   ├── CRNN_Model.keras
    │   │   └── predictor.py
    │   │
    │   ├── services/
    │   │   └── inference.py
    │   │
    │   ├── utils/
    │   │   └── vibration.py
    │   │
    │   └── main.py
    │
    ├── components/
    │   ├── DiagnosisResult.tsx
    │   ├── MainScan.tsx
    │   └── SpectogramViewer.tsx
    │
    ├── guidelines/
    │
    ├── models/
    │
    ├── services/
    │   └── api.ts
    │
    ├── styles/
    │
    ├── utils/
    │
    └── App.tsx
```

### 📂 Backend

Direktori `src/backend/` menangani proses backend dan inference Machine Learning.

| File / Direktori          | Fungsi                               |
| ------------------------- | ------------------------------------ |
| `audio/convert.py`        | Konversi format audio                |
| `audio/preprocess.py`     | Preprocessing data audio             |
| `models/CRNN_Model.keras` | Model Deep Learning                  |
| `models/predictor.py`     | Melakukan prediksi menggunakan model |
| `services/inference.py`   | Menangani proses inference           |
| `utils/vibration.py`      | Utilitas untuk data getaran          |
| `main.py`                 | Entry point API backend              |

### 📂 Frontend

Frontend berada di dalam `src/` dan bertanggung jawab terhadap antarmuka pengguna.

| File / Direktori       | Fungsi                              |
| ---------------------- | ----------------------------------- |
| `App.tsx`              | Entry point aplikasi React          |
| `components/`          | Komponen UI                         |
| `DiagnosisResult.tsx`  | Menampilkan hasil diagnosis         |
| `MainScan.tsx`         | Antarmuka proses scanning           |
| `SpectogramViewer.tsx` | Menampilkan visualisasi spectrogram |
| `services/api.ts`      | Komunikasi frontend dengan backend  |
| `styles/`              | Styling aplikasi                    |
| `utils/`               | Utility frontend                    |
| `models/`              | Model/interface data frontend       |
| `guidelines/`          | Panduan atau informasi diagnosis    |

---

# ⚙️ Persyaratan Sistem

Sebelum menjalankan AUDRIVE, pastikan perangkat telah memiliki software berikut:

* **Node.js**
* **npm**
* **Python**
* **pip**
* **FFmpeg**

### Memeriksa Node.js

Buka Terminal / CMD dan jalankan:

```bash
node -v
```

Kemudian periksa npm:

```bash
npm -v
```

Jika kedua perintah tersebut menampilkan nomor versi, Node.js dan npm telah tersedia.

---

# 🐍 Instalasi Python Dependencies

Pastikan Anda berada pada direktori project yang memiliki file `requirements.txt`.

Kemudian jalankan:

```bash
pip install -r requirements.txt
```

Jika menggunakan Python Launcher pada Windows, Anda juga dapat menggunakan:

```bash
py -m pip install -r requirements.txt
```

---

# 🎵 Instalasi FFmpeg

AUDRIVE membutuhkan **FFmpeg** untuk menangani proses konversi dan pemrosesan audio.

Pastikan FFmpeg telah terinstall dan dapat dipanggil melalui terminal:

```bash
ffmpeg -version
```

Jika perintah tersebut menampilkan informasi versi FFmpeg, instalasi telah berhasil.

> **Note:** Pada Windows, pastikan lokasi `ffmpeg.exe` telah ditambahkan ke environment variable `PATH` agar dapat digunakan dari CMD maupun PowerShell.

---

# 📦 Instalasi Node.js Dependencies

Masuk ke direktori frontend:

```bash
cd src
```

Kemudian install seluruh dependency Node.js:

```bash
npm install
```

---

# 🚀 Menjalankan Aplikasi

AUDRIVE terdiri dari dua layanan utama:

```text
Frontend
   │
   │ HTTP Request
   ▼
Backend API
   │
   ▼
Machine Learning Model
```

Oleh karena itu, **backend harus dijalankan terlebih dahulu**, kemudian frontend.

---

## 1. Menjalankan Backend

Buka Terminal / CMD baru.

Masuk ke direktori backend:

```bash
cd src/backend
```

Kemudian jalankan server:

```bash
py -m uvicorn main:app --reload --port 8000
```

> Jika menggunakan command `python` pada sistem Anda, dapat menggunakan:
>
> ```bash
> python -m uvicorn main:app --reload --port 8000
> ```

Jika berhasil, Uvicorn akan menjalankan API pada:

```text
http://127.0.0.1:8000
```

Dokumentasi API FastAPI biasanya dapat diakses melalui:

```text
http://127.0.0.1:8000/docs
```

Pastikan terminal backend tetap berjalan.

---

## 2. Menjalankan Frontend

Buka **Terminal / CMD baru** dan biarkan terminal backend tetap berjalan.

Masuk ke direktori frontend:

```bash
cd src
```

Kemudian jalankan:

```bash
npm run dev
```

Setelah berhasil, Vite/React akan memberikan alamat lokal pada terminal, biasanya:

```text
http://localhost:5173
```

Buka alamat tersebut menggunakan browser.

---

# 🔄 Alur Menjalankan AUDRIVE

Secara sederhana:

```text
1. Install Node.js
        │
        ▼
2. Install Python
        │
        ▼
3. Install FFmpeg
        │
        ▼
4. Install Python Dependencies
        │
        ▼
5. Install Node Dependencies
        │
        ▼
6. Jalankan Backend
   Port 8000
        │
        ▼
7. Jalankan Frontend
   Port 5173
        │
        ▼
8. Buka Browser
        │
        ▼
      AUDRIVE
```

---

# 🧪 Diagnosis Kendaraan

Secara umum, proses diagnosis AUDRIVE terdiri dari beberapa tahap:

### 1. Input Data

Pengguna memberikan data yang dibutuhkan oleh sistem, seperti:

* Rekaman audio mesin
* Data getaran
* Data telemetri kendaraan

### 2. Preprocessing

Data diproses terlebih dahulu agar sesuai dengan format yang dibutuhkan oleh model Machine Learning.

Contohnya:

```text
Raw Audio
    │
    ▼
Audio Conversion
    │
    ▼
Noise / Signal Processing
    │
    ▼
Feature Extraction
    │
    ▼
Spectrogram
```

### 3. Machine Learning Inference

Data hasil preprocessing diberikan kepada model **CRNN** untuk melakukan klasifikasi.

```text
Processed Audio
       │
       ▼
   CRNN Model
       │
       ▼
 Prediction
```

### 4. Diagnosis

Hasil prediksi kemudian digunakan untuk menghasilkan informasi diagnosis:

```text
┌──────────────────────────┐
│       Diagnosis          │
├──────────────────────────┤
│ Jenis Kerusakan          │
│ Tingkat Keparahan        │
│ Rekomendasi Tindakan     │
│ Estimasi Biaya Servis    │
└──────────────────────────┘
```

---

# 📊 Fitur Utama

* 🎙️ **Audio-based Diagnosis**
* 📈 **Spectrogram Visualization**
* 🤖 **Deep Learning Prediction**
* 🔧 **Engine Fault Classification**
* ⚠️ **Severity Detection**
* 🛠️ **Service Recommendation**
* 💰 **Service Cost Estimation**
* 📡 **Vibration & Telemetry Support**
* 🌐 **Web-based Interface**

---

# 🛠️ Troubleshooting

### Backend tidak dapat dijalankan

Pastikan Anda berada di:

```text
src/backend
```

Kemudian jalankan:

```bash
py -m uvicorn main:app --reload --port 8000
```

Pastikan file berikut tersedia:

```text
src/backend/main.py
```

dan di dalamnya terdapat instance FastAPI yang bernama:

```python
app
```

---

### `pip install` gagal

Pastikan Python dan pip tersedia:

```bash
python --version
pip --version
```

Pada Windows Anda juga dapat menggunakan:

```bash
py --version
py -m pip --version
```

---

### `ffmpeg` tidak ditemukan

Periksa:

```bash
ffmpeg -version
```

Jika muncul pesan seperti:

```text
'ffmpeg' is not recognized...
```

berarti FFmpeg belum tersedia pada `PATH`.

---

### Frontend tidak dapat dijalankan

Pastikan dependency Node.js telah diinstall:

```bash
cd src
npm install
```

Kemudian:

```bash
npm run dev
```

---

# 📌 Catatan Penting

* Jalankan **backend terlebih dahulu** sebelum frontend.
* Pastikan model `CRNN_Model.keras` tersedia di:

```text
src/backend/models/CRNN_Model.keras
```

* Pastikan FFmpeg telah terinstall dan tersedia pada `PATH`.
* Jangan menghapus dependency yang diperlukan oleh backend maupun frontend.
* Untuk pengembangan, gunakan environment Python terpisah/virtual environment agar dependency project tidak bercampur dengan sistem.

---

# 📄 Project Information

**Project:** AUDRIVE
**Tagline:** *Listen Early, Drive Safer*
**Category:** Automotive / Artificial Intelligence / Machine Learning
**Platform:** Web Application
**Backend:** Python / FastAPI
**Frontend:** React / TypeScript
**Machine Learning:** CNN / CRNN
**Audio Processing:** FFmpeg + Python

---

<p align="center">

### 🚗 AUDRIVE

**Listen Early, Drive Safer**

*AI-powered vehicle diagnostics through sound, vibration, and telemetry.*

</p>
