#!/bin/bash
echo "🌾 Installer Aplikasi Input Penjualan"
echo "====================================="

# Cek OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "📱 Windows detected"
    echo "🚀 Menjalankan aplikasi..."
    run_app.bat
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 macOS detected"
    echo "🚀 Menjalankan aplikasi..."
    ./run_app.sh
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Linux detected"
    echo "🚀 Menjalankan aplikasi..."
    ./run_app.sh
else
    echo "❌ OS tidak didukung: $OSTYPE"
    exit 1
fi
