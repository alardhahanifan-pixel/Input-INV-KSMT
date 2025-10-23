#!/bin/bash
echo "🌾 Aplikasi Input Penjualan - Tanpa Python"
echo "=========================================="
echo ""

# Cek OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "📱 Windows detected"
    echo ""
    echo "🚀 Pilihan menjalankan aplikasi:"
    echo "1. Executable (Windows)"
    echo "2. Docker"
    echo "3. Portable Python"
    echo ""
    read -p "Pilih opsi (1-3): " choice
    
    case $choice in
        1)
            echo "🔨 Membuat executable..."
            python build_executable.py
            echo "✅ Executable selesai! Jalankan run_app.bat"
            ;;
        2)
            echo "🐳 Menjalankan dengan Docker..."
            ./build_docker.sh
            docker run -p 8080:8080 -v $(pwd)/instance:/app/instance penjualan-app:latest
            ;;
        3)
            echo "📦 Downloading portable Python..."
            # Script untuk download portable Python
            echo "Silakan download Python portable dari: https://www.python.org/downloads/"
            ;;
        *)
            echo "❌ Pilihan tidak valid"
            ;;
    esac

elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 macOS detected"
    echo ""
    echo "🚀 Pilihan menjalankan aplikasi:"
    echo "1. Executable (macOS)"
    echo "2. Docker"
    echo "3. Homebrew Python"
    echo ""
    read -p "Pilih opsi (1-3): " choice
    
    case $choice in
        1)
            echo "🔨 Membuat executable..."
            python3 build_executable.py
            echo "✅ Executable selesai! Jalankan ./run_app.sh"
            ;;
        2)
            echo "🐳 Menjalankan dengan Docker..."
            ./build_docker.sh
            docker run -p 8080:8080 -v $(pwd)/instance:/app/instance penjualan-app:latest
            ;;
        3)
            echo "📦 Installing dengan Homebrew..."
            if ! command -v brew &> /dev/null; then
                echo "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install python3
            pip3 install -r requirements.txt
            python3 app.py
            ;;
        *)
            echo "❌ Pilihan tidak valid"
            ;;
    esac

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Linux detected"
    echo ""
    echo "🚀 Pilihan menjalankan aplikasi:"
    echo "1. Executable (Linux)"
    echo "2. Docker"
    echo "3. Snap Package"
    echo "4. AppImage"
    echo ""
    read -p "Pilih opsi (1-4): " choice
    
    case $choice in
        1)
            echo "🔨 Membuat executable..."
            python3 build_executable.py
            echo "✅ Executable selesai! Jalankan ./run_app.sh"
            ;;
        2)
            echo "🐳 Menjalankan dengan Docker..."
            ./build_docker.sh
            docker run -p 8080:8080 -v $(pwd)/instance:/app/instance penjualan-app:latest
            ;;
        3)
            echo "📦 Installing dengan Snap..."
            sudo snap install python3 --classic
            pip3 install -r requirements.txt
            python3 app.py
            ;;
        4)
            echo "📦 Membuat AppImage..."
            # Script untuk membuat AppImage
            echo "Membuat AppImage dengan PyInstaller..."
            python3 build_executable.py
            echo "✅ AppImage selesai!"
            ;;
        *)
            echo "❌ Pilihan tidak valid"
            ;;
    esac

else
    echo "❌ OS tidak didukung: $OSTYPE"
    echo "Silakan install Python terlebih dahulu atau gunakan Docker"
    exit 1
fi