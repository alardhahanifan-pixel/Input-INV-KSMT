# 🌾 Aplikasi Input Penjualan

Aplikasi web lokal untuk mengelola data penjualan dengan antarmuka yang user-friendly dan fitur lengkap.

## 🚀 Fitur

- **Form Input Penjualan Lengkap**
  - Data pelanggan (nama, alamat, telepon)
  - Data produk (nama, jumlah, harga)
  - Metode pembayaran
  - Keterangan tambahan
  - Kalkulasi otomatis total harga

- **Manajemen Data**
  - Lihat daftar semua penjualan
  - Edit data penjualan yang sudah tersimpan
  - Hapus data penjualan
  - Pagination untuk data yang banyak

- **Laporan dan Analisis**
  - Statistik total transaksi dan pendapatan
  - Grafik penjualan per bulan
  - Tabel rincian dengan persentase

- **Antarmuka Modern**
  - Desain responsif dengan Bootstrap 5
  - Tema gradient yang menarik
  - Icons Font Awesome
  - Animasi dan transisi halus

## ⚙️ Instalasi dan Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi
```bash
python app.py
```

### 3. Akses Aplikasi
Buka browser dan kunjungi: `http://localhost:8080`

### Alternatif Menjalankan Aplikasi
```bash
# Linux/Mac
./start.sh

# Windows
run.bat

# Atau langsung dengan Python
python3 run.py
```

## 📱 Cara Menggunakan

### Input Penjualan Baru
1. Klik tombol "Input Penjualan" di menu atau halaman beranda
2. Isi form dengan data yang diperlukan:
   - **Tanggal**: Pilih tanggal penjualan
   - **Data Pelanggan**: Nama, alamat, dan nomor telepon
   - **Data Produk**: Nama produk, jumlah, dan harga satuan
   - **Metode Pembayaran**: Pilih dari dropdown
   - **Keterangan**: Catatan tambahan (opsional)
3. Total harga akan dihitung otomatis
4. Klik "Simpan Penjualan"

### Melihat Data Penjualan
1. Klik "Daftar Penjualan" di menu
2. Lihat semua data penjualan dalam tabel
3. Gunakan pagination jika data banyak
4. Klik tombol edit (🖊️) untuk mengubah data
5. Klik tombol hapus (🗑️) untuk menghapus data

### Melihat Laporan
1. Klik "Laporan" di menu
2. Lihat statistik total transaksi dan pendapatan
3. Analisis grafik penjualan per bulan
4. Lihat tabel rincian dengan persentase

## 🗄️ Database

Aplikasi menggunakan SQLite database yang akan dibuat otomatis saat pertama kali dijalankan. File database akan tersimpan sebagai `penjualan.db` di folder aplikasi.

### Struktur Tabel Penjualan
- `id`: Primary key
- `tanggal`: Tanggal penjualan
- `nama_pelanggan`: Nama pelanggan
- `alamat_pelanggan`: Alamat pelanggan
- `no_telepon`: Nomor telepon
- `nama_produk`: Nama produk
- `jumlah`: Jumlah produk
- `harga_satuan`: Harga per satuan
- `total_harga`: Total harga (otomatis)
- `metode_pembayaran`: Metode pembayaran
- `keterangan`: Keterangan tambahan
- `created_at`: Waktu data dibuat

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Database**: SQLite dengan SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Charts**: Chart.js

## 📁 Struktur Proyek

```
/workspace/
├── app.py                 # File utama aplikasi Flask
├── requirements.txt       # Dependencies Python
├── README.md             # Dokumentasi
├── penjualan.db          # Database SQLite (dibuat otomatis)
├── templates/            # Template HTML
│   ├── base.html         # Template dasar
│   ├── index.html        # Halaman beranda
│   ├── input_penjualan.html  # Form input penjualan
│   ├── daftar_penjualan.html # Daftar data penjualan
│   ├── edit_penjualan.html   # Form edit penjualan
│   └── laporan.html      # Halaman laporan
└── static/               # File statis (CSS, JS, images)
    ├── css/
    └── js/
```

## 🔧 Konfigurasi

Aplikasi dapat dikonfigurasi dengan mengubah variabel di `app.py`:

- `SECRET_KEY`: Kunci rahasia untuk session
- `SQLALCHEMY_DATABASE_URI`: URL database
- `host` dan `port`: Alamat dan port server

## 📝 Catatan

- Aplikasi ini dirancang untuk penggunaan lokal
- Data tersimpan dalam database SQLite
- Tidak memerlukan koneksi internet untuk berfungsi
- Cocok untuk usaha kecil dan menengah

## 🤝 Kontribusi

Silakan buka issue atau pull request jika ada saran perbaikan atau fitur tambahan.

## 📄 Lisensi

Aplikasi ini dibuat untuk keperluan pembelajaran dan dapat digunakan secara bebas.