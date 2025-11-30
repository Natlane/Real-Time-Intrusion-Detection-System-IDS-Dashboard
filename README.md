# 🛡️ Real-Time Intrusion Detection System (IDS) + Web Dashboard

**by Kgs Abdul Fatah Revaldo (@Natlane)**

<img width="1920" height="923" alt="image" src="https://github.com/user-attachments/assets/5b4dccb5-642b-46ca-83ad-a1349a6508eb" />

---

## 📖 Deskripsi Project

Project ini adalah **Intrusion Detection System (IDS)** sederhana namun powerful yang berjalan di:

* **Terminal** (alert real-time dari `ids.py`)
* **Web Dashboard realtime** (dari `ids_dashboard.py`)

Project ini memanfaatkan Python + Scapy untuk menangkap paket jaringan dan Flask-SocketIO untuk menampilkan alert & grafik secara langsung lewat browser.

Cocok untuk:
* Latihan analisis paket / IDS sederhana

---

## ⚙️ Fitur-Fitur Utama

### 🛡️ Engine IDS (`ids.py`)

Mendeteksi:

* SYN Scan
* NULL Scan
* XMAS Scan
* Port scanning umum
* Pola paket mencurigakan
* Flooding dasar

Menampilkan:

* Source IP
* Jenis serangan
* Port yang diserang

### 🌐 Real-Time Web Dashboard (`ids_dashboard.py`)

* Menampilkan alert live
* Grafik jumlah paket per menit
* Live update memakai WebSocket (Socket.IO)
* HTML langsung di dalam Python (tidak butuh template folder)

### 🧪 File Testing (`test_ids.py`)

Mempermudah kamu untuk:

* Kirim paket testing
* Lihat respons IDS
* Debugging sebelum uji Nmap

---

## 📂 Struktur Repository

```
📦 ids-real-time
 ┣ 📜 ids.py               # Engine utama IDS
 ┣ 📜 test_ids.py          # Script sederhana untuk ngetes IDS
 ┣ 📜 ids_dashboard.py     # Web dashboard (HTML embed)
 ┣ 📜 README.md            # File dokumentasi
 ┗ 📸 IDS-web-ss.png (placeholder)
 ┗ 📸 IDS-screenshot.png (placeholder)
```

---

## 🛠️ Instalasi

### 1. Clone repository

```bash
git clone https://github.com/Natlane/Real-Time-Intrusion-Detection-System-IDS.git
cd IDS
```

### 2. Buat Virtual Environment (disarankan)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Untuk Kali Linux(karena saya pakai ini di VM):

```bash
pip install flask flask-socketio eventlet scapy --break-system-packages
```

Untuk OS lain:

```bash
pip install flask flask-socketio eventlet scapy
```

---

## 🚀 Cara Menjalankan

### 🛡️ Mode Terminal (IDS CLI)

```bash
sudo python3 ids.py
```

IDS akan mulai mendeteksi paket secara realtime.

---

### 🌐 Mode Web Dashboard

```bash
sudo python3 ids_dashboard.py
```

Lalu buka browser:

```
http://127.0.0.1:5000
```

Kamu akan melihat:

* Alert real-time
* Grafik paket live
* Statistik serangan

---

## 🧪 Testing Serangan (Nmap)

Jalankan commands ini dari mesin lain atau dari VM:

```bash
nmap -sS 127.0.0.1
nmap -sN 127.0.0.1
nmap -sX 127.0.0.1
nmap -F 127.0.0.1
```

IDS akan langsung menampilkan alert di:

* Terminal (ids.py)
* Dashboard (ids_dashboard.py)

---

## 📸 Screenshot (Ganti Nanti)

**Terminal Real-Time:**
![Terminal Screenshot]
<img width="1920" height="923" alt="image" src="https://github.com/user-attachments/assets/c34f0ef8-8d62-4509-a929-9b28eb878c69" />

---

## 🔧 Teknologi yang Digunakan

* Python 3.10
* Scapy
* Flask
* Flask-SocketIO
* Eventlet
* HTML/CSS + Chart.js (embedded)

---

## 👤 Author

**Aldo Aldo**
GitHub: [github.com/aldorefatar](https://github.com/aldorefatar)

---

## ⭐ Support

Kalau project ini membantu, boleh banget kasih **Star ⭐** ke repository-nya!

---
