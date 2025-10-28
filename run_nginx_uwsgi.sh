#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan Nginx + uWSGI..."

# Install nginx and uwsgi if not installed
if ! command -v nginx &> /dev/null; then
    echo "📦 Installing Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi

if ! command -v uwsgi &> /dev/null; then
    echo "📦 Installing uWSGI..."
    pip3 install uwsgi
fi

# Create logs directory
mkdir -p logs

# Copy nginx config
sudo cp nginx_config.conf /etc/nginx/sites-available/penjualan-app
sudo ln -sf /etc/nginx/sites-available/penjualan-app /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test nginx config
sudo nginx -t

# Start uwsgi
uwsgi --ini penjualan-app.ini &

# Start nginx
sudo systemctl start nginx
sudo systemctl enable nginx

echo "✅ Aplikasi berjalan di: http://localhost"
echo "📊 Nginx + uWSGI configuration"
echo "📝 Logs: logs/uwsgi.log dan /var/log/nginx/"
echo ""
echo "🔧 Commands:"
echo "  sudo systemctl status nginx     - Check nginx status"
echo "  sudo systemctl restart nginx    - Restart nginx"
echo "  kill \$(cat logs/uwsgi.pid)      - Stop uwsgi"
echo "  tail -f logs/uwsgi.log          - View uwsgi logs"