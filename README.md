---

# 🛡️ Real-Time Intrusion Detection System (IDS) Dashboard

**by Aldo Aldo (@aldorefatar)**

<img src="screenshot-dashboard.png" width="700" alt="Dashboard Screenshot"/>  
*📌 Ganti dengan screenshot asli setelah project dijalankan*

---

## 📖 Deskripsi Project

Project ini adalah **Intrusion Detection System (IDS)** sederhana berbasis Python yang mampu:

* Mendeteksi serangan jaringan (SYN scan, XMAS scan, NULL scan, dan pola mencurigakan lainnya)
* Menganalisis paket real-time menggunakan **Scapy**
* Menampilkan alert + grafik statistik serangan secara **real-time lewat Web Dashboard**
* Mengirim data live menggunakan **Flask + Socket.IO**

IDS ini ringan, mudah dipahami, dan cocok digunakan sebagai:

* Tugas kampus
* Portfolio GitHub
* Bahan belajar cybersecurity & network monitoring

---

## 🚀 Fitur Utama

### 🔥 **Real-Time Monitoring**

Dashboard web menampilkan:

* Grafik line jumlah paket/menit
* Daftar alert serangan yang muncul live
* Statistik source IP terbanyak

### 🛡️ **Detection Engine**

IDS mampu mendeteksi:

* Port Scan (Nmap)
* SYN Flood
* NULL Scan
* XMAS Scan
* Malformed Packet
* Paket mencurigakan lainnya

### 📊 **Live Traffic Analyzer**

* Paket masuk dihitung per menit
* Disimpan dalam memori untuk membuat grafik real-time

### 🌐 **Web Dashboard**

Dibangun menggunakan:

* Flask
* Socket.IO
* Eventlet
* Chart.js

---

## 📂 Struktur Project

```
📦 ids-dashboard
 ┣ 📜 app.py                # Flask + Socket.IO + IDS logic
 ┣ 📜 ids_core.py           # Engine IDS (jika dipisah)
 ┣ 📜 static/
 │   ┗ 📜 chart.js
 ┣ 📜 templates/
 │   ┗ 📜 index.html        # Web dashboard
 ┣ 📜 README.md
 ┗ 📸 screenshot-dashboard.png (placeholder)
```

---

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/aldorefatar/ids-dashboard.git
cd ids-dashboard
```

### 2. Buat Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

⚠ Kalau menggunakan Kali Linux, gunakan opsi:

```bash
pip install flask flask-socketio eventlet scapy --break-system-packages
```

Atau di venv biasa:

```bash
pip install flask flask-socketio eventlet scapy
```

---

## ▶️ Cara Menjalankan IDS

```bash
sudo python3 app.py
```

Kemudian buka browser:

```
http://127.0.0.1:5000
```

Dashboard akan tampil dan alert akan muncul secara real-time.

---

## 📸 Screenshot (Ganti Dengan Versi Asli)

**Dashboard Realtime:**

![Dashboard](screenshot-dashboard.png)

---

## 🧪 Cara Testing Serangan

Contoh Nmap test:

```bash
nmap -sS 127.0.0.1
nmap -sX 127.0.0.1
nmap -sN 127.0.0.1
```

IDS akan otomatis menampilkan alert.

---

## 🧠 Teknologi yang Digunakan

* Python 3
* Flask
* Flask-SocketIO
* Eventlet
* Scapy
* HTML + CSS + Chart.js

---

## 👤 Author

**Aldo Aldo**
GitHub: [github.com/aldorefatar](https://github.com/aldorefatar)

---

## ⭐ Suka project ini?

Boleh banget kasih **star ⭐ di GitHub** untuk dukungan dan perkembangan selanjutnya!

---

Kalau kamu mau, aku juga bisa:
✅ buatin **preview GIF**
✅ buatin **logo untuk dashboard**
✅ buatin **deskripsi untuk posting LinkedIn**

Tinggal bilang aja!
