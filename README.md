# 🚀 Starter Kit Deploy Vercel (HTML + Python Serverless)

Project latihan siap deploy ke **Vercel** yang dijamin **100% langsung online** tanpa error layar putih (blank) dan tanpa insiden script ter-download!

---

## 📁 Struktur Project

```text
├── index.html           # Tampilan visual website utama (Frontend)
├── vercel.json          # Konfigurasi Vercel
├── README.md            # Panduan ini
└── api/
    └── index.py         # Backend Python (Serverless Function)
```

---

## ❓ Kenapa Kemarin Malah Ter-download & Layar Putih?

1. **Kenapa Script Ter-download?**
   Di Vercel, jika file `.py` ditaruh sembarangan di folder luar (bukan di dalam folder `api/`), Vercel menganggap file tersebut sebagai **dokumen unduhan biasa** (static asset). Akibatnya browser mengunduhnya alih-alih mengeksekusinya.
2. **Kenapa Layar Putih Kosong?**
   Karena Vercel membutuhkan file `index.html` di root repository untuk menampilkan halaman web. Jika tidak ada `index.html`, halaman tidak tahu apa yang harus ditampilkan.

---

## ⚡ Cara Deploy ke Vercel (Untuk Pemula)

1. **Fork atau Clone Repository ini** ke akun GitHub kamu.
2. Buka [vercel.com](https://vercel.com) dan login dengan akun GitHub kamu.
3. Klik tombol **Add New...** ➜ **Project**.
4. Cari dan pilih repository ini, lalu klik **Import**.
5. **Tidak perlu mengubah pengaturan apapun!** Langsung klik tombol **Deploy**.
6. Tunggu beberapa detik, website kamu sudah langsung online dan bisa diakses dunia! 🌐

---

## 🧪 Menguji Backend Python

Setelah website online:
- Buka website kamu.
- Klik tombol **"🐍 Panggil Python Serverless"**.
- Frontend akan otomatis memanggil backend Python di `/api` dan menampilkan respon JSON langsung di layar!
