#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan Supervisor..."

# Install supervisor if not installed
if ! command -v supervisorctl &> /dev/null; then
    echo "📦 Installing Supervisor..."
    sudo apt-get update
    sudo apt-get install -y supervisor
fi

# Create logs directory
mkdir -p logs

# Copy supervisor config
sudo cp penjualan-app.conf /etc/supervisor/conf.d/

# Reload supervisor
sudo supervisorctl reread
sudo supervisorctl update

# Start application
sudo supervisorctl start penjualan-app

echo "✅ Aplikasi berjalan di: http://localhost:8080"
echo ""
echo "🔧 Supervisor Commands:"
echo "  sudo supervisorctl status penjualan-app    - Check status"
echo "  sudo supervisorctl stop penjualan-app     - Stop app"
echo "  sudo supervisorctl start penjualan-app    - Start app"
echo "  sudo supervisorctl restart penjualan-app  - Restart app"
echo "  sudo supervisorctl tail penjualan-app     - View logs"