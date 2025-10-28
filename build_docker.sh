#!/bin/bash
echo "🐳 Membuat Docker Image untuk Aplikasi Input Penjualan"
echo "====================================================="

# Cek apakah Docker terinstall
if ! command -v docker &> /dev/null; then
    echo "❌ Docker tidak terinstall. Silakan install Docker terlebih dahulu."
    echo "   https://docs.docker.com/get-docker/"
    exit 1
fi

# Cek apakah Docker Compose terinstall
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose tidak terinstall. Silakan install Docker Compose terlebih dahulu."
    echo "   https://docs.docker.com/compose/install/"
    exit 1
fi

echo "📦 Building Docker image..."
docker build -f Dockerfile.production -t penjualan-app:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image berhasil dibuat!"
    echo ""
    echo "🚀 Cara menjalankan:"
    echo "   docker run -p 8080:8080 -v \$(pwd)/instance:/app/instance penjualan-app:latest"
    echo ""
    echo "🌐 Atau dengan Docker Compose:"
    echo "   docker-compose -f docker-compose.production.yml up -d"
    echo ""
    echo "📍 Aplikasi akan berjalan di: http://localhost:8080"
else
    echo "❌ Gagal membuat Docker image"
    exit 1
fi