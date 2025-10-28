#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan uWSGI..."

# Install uwsgi if not installed
if ! command -v uwsgi &> /dev/null; then
    echo "📦 Installing uWSGI..."
    pip3 install uwsgi
fi

# Create logs directory
mkdir -p logs

# Start application with uwsgi
uwsgi --ini penjualan-app.ini

echo "✅ Aplikasi berjalan di: http://localhost:8080"
echo "📊 Processes: 4"
echo "📝 Logs: logs/uwsgi.log"
echo "🆔 PID: logs/uwsgi.pid"
echo ""
echo "🔧 Commands:"
echo "  kill \$(cat logs/uwsgi.pid)    - Stop app"
echo "  tail -f logs/uwsgi.log        - View logs"