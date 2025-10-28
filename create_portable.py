#!/usr/bin/env python3
"""
Script untuk membuat portable version dari aplikasi
"""

import os
import sys
import subprocess
import shutil
import zipfile
from pathlib import Path

def create_portable_python():
    """Buat portable Python dengan aplikasi"""
    print("📦 Membuat Portable Python Package...")
    
    # Buat folder portable
    portable_dir = "AplikasiInputPenjualan_Portable"
    if os.path.exists(portable_dir):
        shutil.rmtree(portable_dir)
    
    os.makedirs(portable_dir)
    
    # Copy aplikasi files
    files_to_copy = [
        'app.py',
        'config.py',
        'requirements.txt',
        'demo_data.py',
        'backup_db.py',
        'templates',
        'static',
        'README.md',
        'USAGE.md'
    ]
    
    for item in files_to_copy:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.copytree(item, os.path.join(portable_dir, item))
            else:
                shutil.copy2(item, portable_dir)
    
    # Buat script untuk install Python dependencies
    install_script = '''#!/bin/bash
echo "🌾 Installing Aplikasi Input Penjualan Portable"
echo "=============================================="

# Cek Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan!"
    echo "Silakan install Python3 terlebih dahulu:"
    echo "  Windows: https://www.python.org/downloads/"
    echo "  Linux: sudo apt install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Buat database
echo "🗄️ Creating database..."
python3 -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created!')"

# Tambah data demo
echo "📊 Adding demo data..."
python3 demo_data.py

echo "✅ Installation selesai!"
echo "🚀 Jalankan aplikasi dengan: python3 app.py"
echo "📍 Akses di: http://localhost:8080"
'''
    
    with open(os.path.join(portable_dir, 'install.sh'), 'w') as f:
        f.write(install_script)
    
    os.chmod(os.path.join(portable_dir, 'install.sh'), 0o755)
    
    # Buat script Windows
    install_script_win = '''@echo off
echo 🌾 Installing Aplikasi Input Penjualan Portable
echo ==============================================

REM Cek Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu:
    echo   https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Buat database
echo 🗄️ Creating database...
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created!')"

REM Tambah data demo
echo 📊 Adding demo data...
python demo_data.py

echo ✅ Installation selesai!
echo 🚀 Jalankan aplikasi dengan: python app.py
echo 📍 Akses di: http://localhost:8080
pause
'''
    
    with open(os.path.join(portable_dir, 'install.bat'), 'w') as f:
        f.write(install_script_win)
    
    # Buat README untuk portable
    portable_readme = '''# 🌾 Aplikasi Input Penjualan - Portable Version

## 🚀 Cara Menjalankan

### Windows
1. Double-click `install.bat`
2. Setelah selesai, jalankan: `python app.py`
3. Buka browser ke: http://localhost:8080

### Linux/Mac
1. Buka terminal di folder ini
2. Jalankan: `./install.sh`
3. Setelah selesai, jalankan: `python3 app.py`
4. Buka browser ke: http://localhost:8080

## 📋 Persyaratan
- Python 3.7 atau lebih baru
- pip (package manager Python)

## 🔧 Troubleshooting
- Jika Python tidak ditemukan, install Python dari https://www.python.org/downloads/
- Pastikan Python ditambahkan ke PATH
- Jika ada error, jalankan ulang script install

## 📞 Bantuan
Lihat file README.md untuk dokumentasi lengkap.
'''
    
    with open(os.path.join(portable_dir, 'README_PORTABLE.md'), 'w') as f:
        f.write(portable_readme)
    
    print(f"✅ Portable package berhasil dibuat di: {portable_dir}/")
    
    # Buat ZIP file
    print("📦 Membuat ZIP file...")
    with zipfile.ZipFile(f"{portable_dir}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(portable_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, portable_dir)
                zipf.write(file_path, arcname)
    
    print(f"✅ ZIP file berhasil dibuat: {portable_dir}.zip")

def create_appimage():
    """Buat AppImage untuk Linux"""
    print("📦 Membuat AppImage...")
    
    # Buat folder AppImage
    appimage_dir = "AplikasiInputPenjualan.AppDir"
    if os.path.exists(appimage_dir):
        shutil.rmtree(appimage_dir)
    
    os.makedirs(appimage_dir)
    
    # Copy aplikasi files
    files_to_copy = [
        'app.py',
        'config.py',
        'requirements.txt',
        'demo_data.py',
        'backup_db.py',
        'templates',
        'static'
    ]
    
    for item in files_to_copy:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.copytree(item, os.path.join(appimage_dir, item))
            else:
                shutil.copy2(item, appimage_dir)
    
    # Buat AppRun script
    apprun_content = '''#!/bin/bash
cd "$(dirname "$0")"

# Cek Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan!"
    echo "Silakan install Python3 terlebih dahulu"
    exit 1
fi

# Install dependencies jika belum ada
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Buat database jika belum ada
if [ ! -f "instance/penjualan.db" ]; then
    python3 -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created!')"
    python3 demo_data.py
fi

# Jalankan aplikasi
python3 app.py
'''
    
    with open(os.path.join(appimage_dir, 'AppRun'), 'w') as f:
        f.write(apprun_content)
    
    os.chmod(os.path.join(appimage_dir, 'AppRun'), 0o755)
    
    # Buat desktop file
    desktop_content = '''[Desktop Entry]
Name=Aplikasi Input Penjualan
Comment=Web application for sales input
Exec=AppRun
Icon=logo_padi
Type=Application
Categories=Office;
'''
    
    with open(os.path.join(appimage_dir, 'AplikasiInputPenjualan.desktop'), 'w') as f:
        f.write(desktop_content)
    
    print(f"✅ AppImage directory berhasil dibuat di: {appimage_dir}/")
    print("📝 Untuk membuat AppImage, install appimagetool dan jalankan:")
    print(f"   appimagetool {appimage_dir} AplikasiInputPenjualan-x86_64.AppImage")

def main():
    """Main function"""
    print("🌾 Membuat Portable Version Aplikasi Input Penjualan")
    print("=" * 55)
    
    try:
        # Buat portable Python package
        create_portable_python()
        
        # Buat AppImage jika di Linux
        if sys.platform.startswith('linux'):
            create_appimage()
        
        print("\n✅ Build selesai!")
        print("📁 File yang dibuat:")
        print("   - AplikasiInputPenjualan_Portable/ (folder)")
        print("   - AplikasiInputPenjualan_Portable.zip (ZIP file)")
        if sys.platform.startswith('linux'):
            print("   - AplikasiInputPenjualan.AppDir/ (AppImage directory)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()