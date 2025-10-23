#!/usr/bin/env python3
"""
Script untuk backup dan restore database penjualan
"""

import os
import shutil
from datetime import datetime
from app import app, db, Penjualan

def backup_database():
    """Membuat backup database"""
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_dir}/penjualan_backup_{timestamp}.db"
    
    db_path = "instance/penjualan.db"
    if os.path.exists(db_path):
        shutil.copy2(db_path, backup_file)
        print(f"✅ Backup berhasil dibuat: {backup_file}")
        return backup_file
    else:
        print("❌ Database tidak ditemukan!")
        return None

def restore_database(backup_file):
    """Restore database dari backup"""
    if not os.path.exists(backup_file):
        print(f"❌ File backup tidak ditemukan: {backup_file}")
        return False
    
    # Pastikan folder instance ada
    os.makedirs("instance", exist_ok=True)
    shutil.copy2(backup_file, "instance/penjualan.db")
    print(f"✅ Database berhasil di-restore dari: {backup_file}")
    return True

def list_backups():
    """Menampilkan daftar backup yang tersedia"""
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        print("❌ Folder backup tidak ditemukan!")
        return []
    
    backups = [f for f in os.listdir(backup_dir) if f.endswith('.db')]
    if not backups:
        print("❌ Tidak ada backup yang tersedia!")
        return []
    
    print("📁 Daftar Backup Database:")
    for i, backup in enumerate(backups, 1):
        file_path = os.path.join(backup_dir, backup)
        file_size = os.path.getsize(file_path)
        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        print(f"{i}. {backup} ({file_size} bytes, {file_time.strftime('%Y-%m-%d %H:%M:%S')})")
    
    return backups

def export_to_csv():
    """Export data penjualan ke CSV"""
    with app.app_context():
        penjualan_data = Penjualan.query.all()
        
        if not penjualan_data:
            print("❌ Tidak ada data penjualan untuk diekspor!")
            return
        
        csv_file = f"penjualan_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(csv_file, 'w', encoding='utf-8') as f:
            # Header
            f.write("ID,Tanggal,Nama Pelanggan,Alamat,No Telepon,Nama Produk,Jumlah,Harga Satuan,Total Harga,Metode Pembayaran,Keterangan\n")
            
            # Data
            for p in penjualan_data:
                f.write(f"{p.id},{p.tanggal},{p.nama_pelanggan},{p.alamat_pelanggan or ''},{p.no_telepon or ''},{p.nama_produk},{p.jumlah},{p.harga_satuan},{p.total_harga},{p.metode_pembayaran or ''},{p.keterangan or ''}\n")
        
        print(f"✅ Data berhasil diekspor ke: {csv_file}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("🔧 Penggunaan:")
        print("  python3 backup_db.py backup          - Buat backup database")
        print("  python3 backup_db.py restore <file>  - Restore database")
        print("  python3 backup_db.py list            - Lihat daftar backup")
        print("  python3 backup_db.py export          - Export ke CSV")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "backup":
        backup_database()
    elif command == "restore":
        if len(sys.argv) < 3:
            print("❌ Harap tentukan file backup!")
            sys.exit(1)
        restore_database(sys.argv[2])
    elif command == "list":
        list_backups()
    elif command == "export":
        export_to_csv()
    else:
        print(f"❌ Perintah tidak dikenal: {command}")
        sys.exit(1)