#!/usr/bin/env python3
"""
Script untuk membuat executable dari aplikasi Input Penjualan
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller jika belum ada"""
    try:
        import PyInstaller
        print("✅ PyInstaller sudah terinstall")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def create_spec_file():
    """Buat file spec untuk PyInstaller"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('static', 'static'),
        ('config.py', '.'),
        ('.env.example', '.'),
    ],
    hiddenimports=[
        'flask',
        'flask_sqlalchemy',
        'werkzeug',
        'jinja2',
        'sqlalchemy',
        'datetime',
        'os',
        'json',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AplikasiInputPenjualan',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='logo_padi.png' if os.path.exists('logo_padi.png') else None,
)
'''
    
    with open('AplikasiInputPenjualan.spec', 'w') as f:
        f.write(spec_content)
    
    print("✅ File spec berhasil dibuat")

def build_executable():
    """Build executable dengan PyInstaller"""
    print("🔨 Building executable...")
    
    # Hapus folder build dan dist jika ada
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # Build executable
    subprocess.check_call([
        sys.executable, "-m", "PyInstaller",
        "--clean",
        "--noconfirm",
        "AplikasiInputPenjualan.spec"
    ])
    
    print("✅ Executable berhasil dibuat di folder dist/")

def create_launcher_scripts():
    """Buat script launcher untuk berbagai OS"""
    
    # Windows launcher
    windows_launcher = '''@echo off
echo 🌾 Memulai Aplikasi Input Penjualan...
echo 📍 Aplikasi akan berjalan di: http://localhost:8080
echo ⏹️  Tekan Ctrl+C untuk menghentikan aplikasi
echo --------------------------------------------------
cd /d "%~dp0"
dist\\AplikasiInputPenjualan\\AplikasiInputPenjualan.exe
pause
'''
    
    with open('run_app.bat', 'w') as f:
        f.write(windows_launcher)
    
    # Linux/Mac launcher
    linux_launcher = '''#!/bin/bash
echo "🌾 Memulai Aplikasi Input Penjualan..."
echo "📍 Aplikasi akan berjalan di: http://localhost:8080"
echo "⏹️  Tekan Ctrl+C untuk menghentikan aplikasi"
echo "--------------------------------------------------"
cd "$(dirname "$0")"
./dist/AplikasiInputPenjualan/AplikasiInputPenjualan
'''
    
    with open('run_app.sh', 'w') as f:
        f.write(linux_launcher)
    
    os.chmod('run_app.sh', 0o755)
    
    print("✅ Script launcher berhasil dibuat")

def create_installer_script():
    """Buat script installer"""
    installer_content = '''#!/bin/bash
echo "🌾 Installer Aplikasi Input Penjualan"
echo "====================================="

# Cek OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "📱 Windows detected"
    echo "🚀 Menjalankan aplikasi..."
    run_app.bat
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 macOS detected"
    echo "🚀 Menjalankan aplikasi..."
    ./run_app.sh
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Linux detected"
    echo "🚀 Menjalankan aplikasi..."
    ./run_app.sh
else
    echo "❌ OS tidak didukung: $OSTYPE"
    exit 1
fi
'''
    
    with open('install_and_run.sh', 'w') as f:
        f.write(installer_content)
    
    os.chmod('install_and_run.sh', 0o755)
    
    print("✅ Script installer berhasil dibuat")

def main():
    """Main function"""
    print("🌾 Membuat Executable Aplikasi Input Penjualan")
    print("=" * 50)
    
    try:
        # Install PyInstaller
        install_pyinstaller()
        
        # Buat file spec
        create_spec_file()
        
        # Build executable
        build_executable()
        
        # Buat script launcher
        create_launcher_scripts()
        
        # Buat script installer
        create_installer_script()
        
        print("\n✅ Build selesai!")
        print("📁 Executable tersimpan di: dist/AplikasiInputPenjualan/")
        print("🚀 Jalankan dengan:")
        print("   Windows: run_app.bat")
        print("   Linux/Mac: ./run_app.sh")
        print("   Universal: ./install_and_run.sh")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()