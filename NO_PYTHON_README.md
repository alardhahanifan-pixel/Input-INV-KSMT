# 🌾 Aplikasi Input Penjualan - Tanpa Python

Aplikasi ini dapat dijalankan tanpa perlu menginstall Python terlebih dahulu menggunakan beberapa metode:

## 🚀 Metode 1: Executable (Recommended)

### Windows
```bash
# Buat executable
python build_executable.py

# Jalankan executable
run_app.bat
```

### Linux/Mac
```bash
# Buat executable
python3 build_executable.py

# Jalankan executable
./run_app.sh
```

## 🐳 Metode 2: Docker

### Prerequisites
- Docker Desktop terinstall
- Docker Compose terinstall

### Cara Menjalankan
```bash
# Build Docker image
./build_docker.sh

# Jalankan dengan Docker
docker run -p 8080:8080 -v $(pwd)/instance:/app/instance penjualan-app:latest

# Atau dengan Docker Compose
docker-compose -f docker-compose.production.yml up -d
```

## 📦 Metode 3: Portable Package

### Buat Portable Package
```bash
python3 create_portable.py
```

### Distribusi
- **AplikasiInputPenjualan_Portable.zip** - Package lengkap
- **AplikasiInputPenjualan_Portable/** - Folder portable

### Cara Menggunakan
1. Extract ZIP file
2. Jalankan `install.bat` (Windows) atau `./install.sh` (Linux/Mac)
3. Setelah selesai, jalankan `python app.py`

## 🖥️ Metode 4: AppImage (Linux)

### Buat AppImage
```bash
# Install appimagetool
sudo apt install appimagetool

# Buat AppImage
python3 create_portable.py
appimagetool AplikasiInputPenjualan.AppDir AplikasiInputPenjualan-x86_64.AppImage
```

### Jalankan AppImage
```bash
chmod +x AplikasiInputPenjualan-x86_64.AppImage
./AplikasiInputPenjualan-x86_64.AppImage
```

## 🎯 Metode 5: Script Otomatis

### Jalankan Script Otomatis
```bash
./run_without_python.sh
```

Script ini akan:
- Mendeteksi OS Anda
- Memberikan pilihan metode yang sesuai
- Membuat executable atau menjalankan dengan Docker

## 📋 Persyaratan Sistem

### Executable
- **Windows**: Windows 7/8/10/11 (64-bit)
- **Linux**: Ubuntu 18.04+ atau distro Linux modern
- **macOS**: macOS 10.14+ (Mojave atau lebih baru)

### Docker
- **Windows**: Docker Desktop for Windows
- **Linux**: Docker Engine + Docker Compose
- **macOS**: Docker Desktop for Mac

### Portable Package
- Python 3.7+ (akan diinstall otomatis)
- pip (package manager Python)

## 🔧 Troubleshooting

### Executable tidak berjalan
```bash
# Cek permission (Linux/Mac)
chmod +x run_app.sh

# Cek antivirus (Windows)
# Tambahkan folder ke whitelist antivirus
```

### Docker error
```bash
# Cek Docker status
docker --version
docker-compose --version

# Restart Docker
sudo systemctl restart docker
```

### Portable package error
```bash
# Cek Python
python3 --version

# Install Python jika belum ada
# Windows: https://www.python.org/downloads/
# Linux: sudo apt install python3 python3-pip
# macOS: brew install python3
```

## 📁 File yang Dibuat

### Executable
- `dist/AplikasiInputPenjualan/` - Folder executable
- `run_app.bat` - Launcher Windows
- `run_app.sh` - Launcher Linux/Mac
- `install_and_run.sh` - Universal launcher

### Docker
- `penjualan-app:latest` - Docker image
- `docker-compose.production.yml` - Docker Compose config
- `nginx_production.conf` - Nginx config

### Portable
- `AplikasiInputPenjualan_Portable/` - Folder portable
- `AplikasiInputPenjualan_Portable.zip` - ZIP file
- `AplikasiInputPenjualan.AppDir/` - AppImage directory

## 🎉 Keuntungan

### Executable
- ✅ Tidak perlu Python
- ✅ Mudah didistribusi
- ✅ Cepat startup
- ❌ File besar

### Docker
- ✅ Konsisten di semua OS
- ✅ Mudah deployment
- ✅ Isolated environment
- ❌ Perlu Docker

### Portable Package
- ✅ Mudah digunakan
- ✅ Include Python
- ✅ Cross-platform
- ❌ Perlu Python

## 📞 Bantuan

Jika mengalami masalah:
1. Cek log error di terminal
2. Pastikan port 8080 tidak digunakan
3. Cek firewall/antivirus
4. Restart aplikasi

## 🔄 Update

Untuk update aplikasi:
1. Download versi terbaru
2. Ganti file yang ada
3. Restart aplikasi

## 📄 Lisensi

Aplikasi ini gratis dan open source. Dapat digunakan untuk keperluan komersial maupun non-komersial.