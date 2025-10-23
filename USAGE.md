# 📖 Panduan Penggunaan Aplikasi Input Penjualan

## 🚀 Memulai Aplikasi

### Cara 1: Menggunakan Script Otomatis
```bash
# Linux/Mac
./start.sh

# Windows
run.bat

# Atau dengan Python
python3 run.py
```

### Cara 2: Manual
```bash
# Install dependencies
pip3 install -r requirements.txt

# Jalankan aplikasi
python3 app.py
```

### Cara 3: Mode Production
```bash
python3 run_production.py
```

## 📱 Menggunakan Aplikasi

### 1. Halaman Beranda
- **URL**: `http://localhost:8080`
- **Fitur**: 
  - Menu navigasi ke semua fitur
  - Statistik ringkas
  - Akses cepat ke fitur utama

### 2. Input Penjualan Baru
- **URL**: `http://localhost:8080/input_penjualan`
- **Cara Menggunakan**:
  1. Isi tanggal penjualan (default: hari ini)
  2. Pilih metode pembayaran dari dropdown
  3. Isi data pelanggan (nama wajib, alamat dan telepon opsional)
  4. Isi data produk (nama, jumlah, harga satuan)
  5. Total harga akan dihitung otomatis
  6. Tambahkan keterangan jika perlu
  7. Klik "Simpan Penjualan"

### 3. Daftar Penjualan
- **URL**: `http://localhost:8080/daftar_penjualan`
- **Fitur**:
  - Tampilkan semua data penjualan dalam tabel
  - Pagination untuk data yang banyak
  - Tombol edit (🖊️) untuk mengubah data
  - Tombol hapus (🗑️) untuk menghapus data
  - Konfirmasi sebelum menghapus

### 4. Edit Penjualan
- **URL**: `http://localhost:8080/edit_penjualan/<id>`
- **Cara Menggunakan**:
  1. Klik tombol edit di daftar penjualan
  2. Ubah data yang diperlukan
  3. Total harga akan dihitung ulang otomatis
  4. Klik "Update Penjualan"

### 5. Laporan Penjualan
- **URL**: `http://localhost:8080/laporan`
- **Fitur**:
  - Statistik total transaksi dan pendapatan
  - Grafik penjualan per bulan
  - Tabel rincian dengan persentase
  - Visualisasi data yang interaktif

## 🗄️ Manajemen Database

### Backup Database
```bash
# Buat backup
python3 backup_db.py backup

# Lihat daftar backup
python3 backup_db.py list

# Restore dari backup
python3 backup_db.py restore backups/penjualan_backup_20240101_120000.db
```

### Export Data
```bash
# Export ke CSV
python3 backup_db.py export
```

### Data Demo
```bash
# Tambahkan data demo untuk testing
python3 demo_data.py
```

## ⚙️ Konfigurasi

### Environment Variables
Buat file `.env` berdasarkan `.env.example`:
```bash
cp .env.example .env
```

Edit file `.env`:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///penjualan.db
HOST=0.0.0.0
PORT=8080
DEBUG=True
```

### Konfigurasi Database
- **Development**: SQLite (default)
- **Production**: Bisa diganti ke PostgreSQL/MySQL dengan mengubah `DATABASE_URL`

## 🔧 Troubleshooting

### Port Sudah Digunakan
```bash
# Cek port yang digunakan
lsof -i :8080

# Atau ubah port di config.py
PORT=8081
```

### Database Error
```bash
# Hapus database dan buat ulang
rm -rf instance/
python3 demo_data.py
```

### Dependencies Error
```bash
# Install ulang dependencies
pip3 install -r requirements.txt --force-reinstall
```

## 📊 Struktur Data

### Tabel Penjualan
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| tanggal | Date | Tanggal penjualan |
| nama_pelanggan | String(100) | Nama pelanggan |
| alamat_pelanggan | String(200) | Alamat pelanggan |
| no_telepon | String(20) | Nomor telepon |
| nama_produk | String(100) | Nama produk |
| jumlah | Integer | Jumlah produk |
| harga_satuan | Float | Harga per satuan |
| total_harga | Float | Total harga |
| metode_pembayaran | String(50) | Metode pembayaran |
| keterangan | Text | Keterangan tambahan |
| created_at | DateTime | Waktu data dibuat |

## 🎯 Tips Penggunaan

### 1. Input Data yang Efisien
- Gunakan data pelanggan yang konsisten
- Simpan template produk yang sering dijual
- Gunakan keterangan untuk catatan penting

### 2. Backup Rutin
- Lakukan backup database secara berkala
- Simpan backup di lokasi yang aman
- Test restore untuk memastikan backup valid

### 3. Analisis Data
- Gunakan laporan untuk melihat tren penjualan
- Identifikasi produk yang paling laris
- Pantau metode pembayaran yang populer

### 4. Keamanan
- Ganti SECRET_KEY di production
- Backup database secara rutin
- Jangan share file database

## 🆘 Bantuan

Jika mengalami masalah:
1. Periksa log error di terminal
2. Pastikan semua dependencies terinstall
3. Cek konfigurasi database
4. Restart aplikasi jika perlu

## 📞 Support

Untuk bantuan lebih lanjut, silakan buka issue di repository atau hubungi developer.