#!/bin/bash
echo "🌾 Memulai Aplikasi Input Penjualan..."
echo "📍 Aplikasi akan berjalan di: http://localhost:8080"
echo "⏹️  Tekan Ctrl+C untuk menghentikan aplikasi"
echo "--------------------------------------------------"

# Cek apakah Python 3 tersedia
if command -v python3 &> /dev/null; then
    python3 app.py
elif command -v python &> /dev/null; then
    python app.py
else
    echo "❌ Python tidak ditemukan. Silakan install Python terlebih dahulu."
    exit 1
fi