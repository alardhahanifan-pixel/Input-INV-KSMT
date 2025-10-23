#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan PM2..."

# Install PM2 if not installed
if ! command -v pm2 &> /dev/null; then
    echo "📦 Installing PM2..."
    npm install -g pm2
fi

# Create logs directory
mkdir -p logs

# Start application
pm2 start ecosystem.config.js

echo "✅ Aplikasi berjalan di: http://localhost:8080"
echo ""
echo "🔧 PM2 Commands:"
echo "  pm2 status                    - Check status"
echo "  pm2 stop penjualan-app       - Stop app"
echo "  pm2 restart penjualan-app    - Restart app"
echo "  pm2 logs penjualan-app       - View logs"
echo "  pm2 monit                     - Monitor"
echo "  pm2 delete penjualan-app     - Remove app"