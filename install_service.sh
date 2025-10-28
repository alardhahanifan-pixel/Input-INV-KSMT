#!/bin/bash
echo "🔧 Installing Aplikasi Input Penjualan as systemd service..."

# Copy service file
sudo cp penjualan-app.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable penjualan-app

# Start service
sudo systemctl start penjualan-app

echo "✅ Service installed and started!"
echo "📍 Aplikasi berjalan di: http://localhost:8080"
echo ""
echo "🔧 Commands:"
echo "  sudo systemctl status penjualan-app    - Check status"
echo "  sudo systemctl stop penjualan-app     - Stop service"
echo "  sudo systemctl start penjualan-app    - Start service"
echo "  sudo systemctl restart penjualan-app  - Restart service"
echo "  sudo systemctl disable penjualan-app  - Disable service"