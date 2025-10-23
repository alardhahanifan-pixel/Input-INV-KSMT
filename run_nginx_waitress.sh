#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan Nginx + Waitress..."

# Install nginx and waitress if not installed
if ! command -v nginx &> /dev/null; then
    echo "📦 Installing Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi

if ! python3 -c "import waitress" 2>/dev/null; then
    echo "📦 Installing Waitress..."
    pip3 install waitress
fi

# Create logs directory
mkdir -p logs

# Copy nginx config
sudo cp nginx_gunicorn_config.conf /etc/nginx/sites-available/penjualan-app
sudo ln -sf /etc/nginx/sites-available/penjualan-app /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test nginx config
sudo nginx -t

# Start waitress
python3 run_waitress.py &

# Start nginx
sudo systemctl start nginx
sudo systemctl enable nginx

echo "✅ Aplikasi berjalan di: http://localhost"
echo "📊 Nginx + Waitress configuration"
echo "📝 Logs: /var/log/nginx/"
echo ""
echo "🔧 Commands:"
echo "  sudo systemctl status nginx     - Check nginx status"
echo "  sudo systemctl restart nginx    - Restart nginx"
echo "  pkill -f run_waitress.py        - Stop waitress"