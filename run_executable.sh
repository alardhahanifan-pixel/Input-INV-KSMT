#!/bin/bash
echo "🌾 Menjalankan Aplikasi Input Penjualan (Executable)"
echo "===================================================="

# Cek apakah executable ada
if [ ! -f "dist/AplikasiInputPenjualan" ]; then
    echo "❌ Executable tidak ditemukan!"
    echo "Jalankan: python3 build_executable.py"
    exit 1
fi

# Cek port yang tersedia
PORT=8080
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
    PORT=$((PORT + 1))
done

echo "📍 Menggunakan port: $PORT"
echo "🌐 Aplikasi akan berjalan di: http://localhost:$PORT"
echo "⏹️  Tekan Ctrl+C untuk menghentikan aplikasi"
echo "--------------------------------------------------"

# Set environment variable untuk port
export PORT=$PORT

# Jalankan executable
./dist/AplikasiInputPenjualan