@echo off
echo 🌾 Memulai Aplikasi Input Penjualan...
echo 📍 Aplikasi akan berjalan di: http://localhost:8080
echo ⏹️  Tekan Ctrl+C untuk menghentikan aplikasi
echo --------------------------------------------------
cd /d "%~dp0"
dist\AplikasiInputPenjualan\AplikasiInputPenjualan.exe
pause
