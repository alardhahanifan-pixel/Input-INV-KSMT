#!/bin/bash
echo "🐳 Menjalankan Aplikasi Input Penjualan dengan Docker..."

# Build image
echo "📦 Building Docker image..."
docker build -t penjualan-app .

# Run container
echo "🚀 Starting container..."
docker run -d \
  --name penjualan-app \
  -p 8080:8080 \
  -v $(pwd)/instance:/app/instance \
  -v $(pwd)/backups:/app/backups \
  penjualan-app

echo "✅ Aplikasi berjalan di: http://localhost:8080"
echo "⏹️  Untuk menghentikan: docker stop penjualan-app"
echo "🗑️  Untuk menghapus: docker rm penjualan-app"