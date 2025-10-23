from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from config import config

app = Flask(__name__)

# Konfigurasi aplikasi
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

db = SQLAlchemy(app)

# Model untuk database
class Penjualan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date, nullable=False)
    nama_pelanggan = db.Column(db.String(100), nullable=False)
    alamat_pelanggan = db.Column(db.String(200))
    no_telepon = db.Column(db.String(20))
    nama_produk = db.Column(db.String(100), nullable=False)
    jumlah = db.Column(db.Integer, nullable=False)
    harga_satuan = db.Column(db.Float, nullable=False)
    total_harga = db.Column(db.Float, nullable=False)
    metode_pembayaran = db.Column(db.String(50))
    keterangan = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Penjualan {self.nama_pelanggan} - {self.nama_produk}>'

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input_penjualan', methods=['GET', 'POST'])
def input_penjualan():
    if request.method == 'POST':
        try:
            # Ambil data dari form
            tanggal = datetime.strptime(request.form['tanggal'], '%Y-%m-%d').date()
            nama_pelanggan = request.form['nama_pelanggan']
            alamat_pelanggan = request.form['alamat_pelanggan']
            no_telepon = request.form['no_telepon']
            nama_produk = request.form['nama_produk']
            jumlah = int(request.form['jumlah'])
            harga_satuan = float(request.form['harga_satuan'])
            total_harga = float(request.form['total_harga'])
            metode_pembayaran = request.form['metode_pembayaran']
            keterangan = request.form['keterangan']

            # Buat record baru
            penjualan = Penjualan(
                tanggal=tanggal,
                nama_pelanggan=nama_pelanggan,
                alamat_pelanggan=alamat_pelanggan,
                no_telepon=no_telepon,
                nama_produk=nama_produk,
                jumlah=jumlah,
                harga_satuan=harga_satuan,
                total_harga=total_harga,
                metode_pembayaran=metode_pembayaran,
                keterangan=keterangan
            )

            db.session.add(penjualan)
            db.session.commit()
            flash('Data penjualan berhasil disimpan!', 'success')
            return redirect(url_for('daftar_penjualan'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            return redirect(url_for('input_penjualan'))
    
    return render_template('input_penjualan.html')

@app.route('/daftar_penjualan')
def daftar_penjualan():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    penjualan = Penjualan.query.order_by(Penjualan.tanggal.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('daftar_penjualan.html', penjualan=penjualan)

@app.route('/edit_penjualan/<int:id>', methods=['GET', 'POST'])
def edit_penjualan(id):
    penjualan = Penjualan.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            penjualan.tanggal = datetime.strptime(request.form['tanggal'], '%Y-%m-%d').date()
            penjualan.nama_pelanggan = request.form['nama_pelanggan']
            penjualan.alamat_pelanggan = request.form['alamat_pelanggan']
            penjualan.no_telepon = request.form['no_telepon']
            penjualan.nama_produk = request.form['nama_produk']
            penjualan.jumlah = int(request.form['jumlah'])
            penjualan.harga_satuan = float(request.form['harga_satuan'])
            penjualan.total_harga = float(request.form['total_harga'])
            penjualan.metode_pembayaran = request.form['metode_pembayaran']
            penjualan.keterangan = request.form['keterangan']
            
            db.session.commit()
            flash('Data penjualan berhasil diperbarui!', 'success')
            return redirect(url_for('daftar_penjualan'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
    
    return render_template('edit_penjualan.html', penjualan=penjualan)

@app.route('/hapus_penjualan/<int:id>')
def hapus_penjualan(id):
    penjualan = Penjualan.query.get_or_404(id)
    db.session.delete(penjualan)
    db.session.commit()
    flash('Data penjualan berhasil dihapus!', 'success')
    return redirect(url_for('daftar_penjualan'))

@app.route('/laporan')
def laporan():
    # Hitung statistik
    total_penjualan = Penjualan.query.count()
    total_pendapatan = db.session.query(db.func.sum(Penjualan.total_harga)).scalar() or 0
    
    # Data untuk chart (penjualan per bulan)
    penjualan_per_bulan = db.session.query(
        db.func.strftime('%Y-%m', Penjualan.tanggal).label('bulan'),
        db.func.sum(Penjualan.total_harga).label('total')
    ).group_by('bulan').order_by('bulan').all()
    
    return render_template('laporan.html', 
                         total_penjualan=total_penjualan,
                         total_pendapatan=total_pendapatan,
                         penjualan_per_bulan=penjualan_per_bulan)

# API untuk mendapatkan data penjualan (untuk AJAX)
@app.route('/api/penjualan')
def api_penjualan():
    penjualan = Penjualan.query.order_by(Penjualan.tanggal.desc()).all()
    return jsonify([{
        'id': p.id,
        'tanggal': p.tanggal.strftime('%Y-%m-%d'),
        'nama_pelanggan': p.nama_pelanggan,
        'nama_produk': p.nama_produk,
        'jumlah': p.jumlah,
        'harga_satuan': p.harga_satuan,
        'total_harga': p.total_harga,
        'metode_pembayaran': p.metode_pembayaran
    } for p in penjualan])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])