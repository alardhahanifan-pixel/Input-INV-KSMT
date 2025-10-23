#!/usr/bin/env python3
"""
Script untuk menjalankan aplikasi dalam mode production
"""

import os
import sys

# Set environment ke production
os.environ['FLASK_ENV'] = 'production'

# Pastikan kita berada di direktori yang benar
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import dan jalankan aplikasi
from app import app

if __name__ == '__main__':
    print("🌾 Memulai Aplikasi Input Penjualan (Production Mode)...")
    print("📍 Aplikasi akan berjalan di: http://localhost:8080")
    print("⏹️  Tekan Ctrl+C untuk menghentikan aplikasi")
    print("-" * 50)
    
    try:
        app.run(debug=False, host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print("\n👋 Aplikasi dihentikan. Terima kasih!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)