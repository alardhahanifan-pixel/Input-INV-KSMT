#!/bin/bash
echo "🚀 Menjalankan Aplikasi Input Penjualan dengan Gunicorn..."

# Install gunicorn if not installed
if ! command -v gunicorn &> /dev/null; then
    echo "📦 Installing Gunicorn..."
    pip3 install gunicorn
fi

# Create logs directory
mkdir -p logs

# Start application with gunicorn
gunicorn --bind 0.0.0.0:8080 \
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

echo "✅ Aplikasi berjalan di: http://localhost:8080"
echo "📊 Workers: 4"
echo "📝 Logs: logs/access.log dan logs/error.log"
echo "🆔 PID: logs/gunicorn.pid"
echo ""
echo "🔧 Commands:"
echo "  kill \$(cat logs/gunicorn.pid)  - Stop app"
echo "  tail -f logs/access.log        - View access logs"
echo "  tail -f logs/error.log         - View error logs"