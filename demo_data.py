#!/usr/bin/env python3
"""
Script untuk menambahkan data demo ke aplikasi penjualan
"""

from app import app, db, Penjualan
from datetime import datetime, timedelta
import random

def create_demo_data():
    """Membuat data demo untuk testing aplikasi"""
    
    with app.app_context():
        # Buat database jika belum ada
        db.create_all()
        
        # Data demo
        demo_data = [
            {
                'tanggal': datetime.now().date() - timedelta(days=1),
                'nama_pelanggan': 'Ahmad Wijaya',
                'alamat_pelanggan': 'Jl. Merdeka No. 123, Jakarta',
                'no_telepon': '081234567890',
                'nama_produk': 'Beras Premium 5kg',
                'jumlah': 2,
                'harga_satuan': 45000,
                'total_harga': 90000,
                'metode_pembayaran': 'Transfer Bank',
                'keterangan': 'Pembayaran lunas'
            },
            {
                'tanggal': datetime.now().date() - timedelta(days=2),
                'nama_pelanggan': 'Siti Nurhaliza',
                'alamat_pelanggan': 'Jl. Sudirman No. 456, Bandung',
                'no_telepon': '081234567891',
                'nama_produk': 'Minyak Goreng 1L',
                'jumlah': 5,
                'harga_satuan': 15000,
                'total_harga': 75000,
                'metode_pembayaran': 'Tunai',
                'keterangan': 'Pelanggan tetap'
            },
            {
                'tanggal': datetime.now().date() - timedelta(days=3),
                'nama_pelanggan': 'Budi Santoso',
                'alamat_pelanggan': 'Jl. Gatot Subroto No. 789, Surabaya',
                'no_telepon': '081234567892',
                'nama_produk': 'Gula Pasir 1kg',
                'jumlah': 10,
                'harga_satuan': 12000,
                'total_harga': 120000,
                'metode_pembayaran': 'E-Wallet',
                'keterangan': 'Bulk order'
            },
            {
                'tanggal': datetime.now().date() - timedelta(days=4),
                'nama_pelanggan': 'Dewi Sartika',
                'alamat_pelanggan': 'Jl. Thamrin No. 321, Medan',
                'no_telepon': '081234567893',
                'nama_produk': 'Telur Ayam 1kg',
                'jumlah': 3,
                'harga_satuan': 25000,
                'total_harga': 75000,
                'metode_pembayaran': 'Kartu Debit',
                'keterangan': 'Order pagi'
            },
            {
                'tanggal': datetime.now().date() - timedelta(days=5),
                'nama_pelanggan': 'Rudi Hartono',
                'alamat_pelanggan': 'Jl. Diponegoro No. 654, Yogyakarta',
                'no_telepon': '081234567894',
                'nama_produk': 'Susu UHT 1L',
                'jumlah': 4,
                'harga_satuan': 18000,
                'total_harga': 72000,
                'metode_pembayaran': 'Transfer Bank',
                'keterangan': 'Order keluarga'
            }
        ]
        
        # Tambahkan data ke database
        for data in demo_data:
            penjualan = Penjualan(**data)
            db.session.add(penjualan)
        
        db.session.commit()
        print("✅ Data demo berhasil ditambahkan!")
        print(f"📊 Total data: {len(demo_data)} penjualan")
        print("🌐 Jalankan aplikasi dengan: python3 app.py")
        print("📍 Akses di: http://localhost:8080")

if __name__ == '__main__':
    create_demo_data()