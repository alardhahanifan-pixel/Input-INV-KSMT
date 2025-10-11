import streamlit as st
import pandas as pd
import tempfile
import zipfile
import os
import requests
from io import BytesIO
from openpyxl import load_workbook

# === KONFIGURASI DASAR ===
st.set_page_config(
    page_title="Input Invoice Penjualan KSMT",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === GAYA TAMPAK DEPAN ===
st.markdown("""
    <style>
        body { background-color: #0e1117; color: #fafafa; }
        .stApp { background-color: #0e1117; }
        .title { text-align:center; color:#f1f1f1; font-size:32px; font-weight:bold; margin-top:-20px; }
        .sub { text-align:center; color:#aaa; margin-bottom:30px; }
        .stButton>button { background-color:#1f6f43; color:white; border:none; padding:0.6em 1.2em; border-radius:10px; }
        .stButton>button:hover { background-color:#268a54; }
    </style>
""", unsafe_allow_html=True)

# === HEADER & LOGO ===
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("logo_padi.png", width=150)
st.markdown("<div class='title'>Input Invoice Penjualan KSMT</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Ekstrak data otomatis dari foto invoice ke Excel Template</div>", unsafe_allow_html=True)

# === INPUT FILE ===
uploaded_file = st.file_uploader("Upload file ZIP berisi foto invoice (.zip)", type=["zip"])

# === EXTRACT TEXT FROM IMAGE ===
def extract_text_from_image(image_bytes):
    """Ekstraksi teks dari gambar menggunakan OCR.space"""
    url = "https://api.ocr.space/parse/image"
    payload = {
        "apikey": "helloworld",  # ganti dengan API key kamu jika punya
        "language": "ind",
    }
    files = {"file": image_bytes}
    response = requests.post(url, files=files, data=payload)
    
    try:
        result = response.json()
    except Exception as e:
        st.error(f"Gagal membaca hasil dari OCR.space: {e}")
        return ""
    
    # cek error dari API
    if result.get("IsErroredOnProcessing"):
        st.warning(f"❌ OCR gagal memproses gambar: {result.get('ErrorMessage', 'Tidak diketahui')}")
        return ""
    
    parsed_results = result.get("ParsedResults")
    if not parsed_results:
        st.warning("❌ Tidak ada teks yang berhasil diekstrak dari gambar ini.")
        st.text_area("Respon OCR:", json.dumps(result, indent=2))
        return ""
    
    # ambil teks
    return parsed_results[0].get("ParsedText", "")


# === EKSEKUSI ===
if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, uploaded_file.name)
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Ekstrak file ZIP
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)
            st.success("📦 File ZIP berhasil diekstrak!")
        except Exception as e:
            st.error(f"❌ Gagal mengekstrak ZIP: {e}")
            st.stop()

        st.info("📸 Membaca gambar invoice dan menjalankan OCR...")

        all_texts = []
        for root, _, files in os.walk(tmpdir):
            for img_file in files:
                if img_file.lower().endswith((".jpg", ".jpeg", ".png")):
                    with open(os.path.join(root, img_file), "rb") as img:
                        text = extract_text_from_image(img)
                        all_texts.append(text)

        st.success(f"✅ Berhasil membaca {len(all_texts)} gambar invoice!")

        # --- Simulasi hasil olahan ---
        data = {
            "Nama": ["Beras Ladang Padi", "Ketan Pesona Laut", "Katul", "Sekam Giling"],
            "Kemasan": ["25", "-", "-", "-"],
            "Berat": ["10+15", "20", "30", "40"],
            "Harga": ["", "12000", "1500", "1000"],
            "Jumlah": ["=10+15", "=20*12000", "=30*1500", "=40*1000"]
        }
        df = pd.DataFrame(data)

        st.subheader("📋 Hasil Rekap Otomatis (Contoh Data Simulasi)")
        st.dataframe(df)

        # === LOAD TEMPLATE & TULIS DATA ===
        template_path = "Template.xlsx"
        wb = load_workbook(template_path)
        ws = wb.active

        start_row = 2
        for i, row in df.iterrows():
            ws.cell(row=start_row+i, column=1, value=row["Nama"])
            ws.cell(row=start_row+i, column=2, value=row["Berat"])
            ws.cell(row=start_row+i, column=3, value=row["Harga"])
            ws.cell(row=start_row+i, column=4, value=row["Jumlah"])

        output_path = os.path.join(tmpdir, "Rekap_Invoice.xlsx")
        wb.save(output_path)

        # === DOWNLOAD BUTTON ===
        with open(output_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Rekap Excel",
                data=f,
                file_name="Rekap_Invoice.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.success("✅ Proses selesai! Silakan unduh hasil rekap di atas.")
