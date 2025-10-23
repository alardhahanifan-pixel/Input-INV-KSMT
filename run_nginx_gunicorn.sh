#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan Nginx + Gunicorn..."

# Install nginx and gunicorn if not installed
if ! command -v nginx &> /dev/null; then
    echo "📦 Installing Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi

if ! command -v gunicorn &> /dev/null; then
    echo "📦 Installing Gunicorn..."
    pip3 install gunicorn
fi

# Create logs directory
mkdir -p logs

# Copy nginx config
sudo cp nginx_gunicorn_config.conf /etc/nginx/sites-available/penjualan-app
sudo ln -sf /etc/nginx/sites-available/penjualan-app /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test nginx config
sudo nginx -t

# Start gunicorn
gunicorn --bind 127.0.0.1:8080 \
         --workers 4 \
         --worker-class sync \
         --timeout 120 \
         --keep-alive 2 \
         --max-requests 1000 \
         --max-requests-jitter 100 \
         --access-logfile logs/access.log \
         --error-logfile logs/error.log \
         --log-level info \
         --pid logs/gunicorn.pid \
         --daemon \
         app:app

# Start nginx
sudo systemctl start nginx
sudo systemctl enable nginx

echo "✅ Aplikasi berjalan di: http://localhost"
echo "📊 Nginx + Gunicorn configuration"
echo "📝 Logs: logs/access.log, logs/error.log dan /var/log/nginx/"
echo ""
echo "🔧 Commands:"
echo "  sudo systemctl status nginx     - Check nginx status"
echo "  sudo systemctl restart nginx    - Restart nginx"
echo "  kill \$(cat logs/gunicorn.pid)   - Stop gunicorn"
echo "  tail -f logs/access.log         - View access logs"