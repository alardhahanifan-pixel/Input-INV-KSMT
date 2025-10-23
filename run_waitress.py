#!/usr/bin/env python3
"""
Script untuk menjalankan aplikasi dengan Waitress (Windows-compatible)
"""

import os
import sys
from waitress import serve

# Pastikan kita berada di direktori yang benar
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import aplikasi
from app import app

if __name__ == '__main__':
    print("🌾 Memulai Aplikasi Input Penjualan dengan Waitress...")
    print("📍 Aplikasi akan berjalan di: http://localhost:8080")
    print("⏹️  Tekan Ctrl+C untuk menghentikan aplikasi")
    print("-" * 50)
    
    try:
        # Jalankan dengan Waitress
        serve(app, host='0.0.0.0', port=8080, threads=4)
    except KeyboardInterrupt:
        print("\n👋 Aplikasi dihentikan. Terima kasih!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)