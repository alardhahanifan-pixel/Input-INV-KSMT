import os
import io
import zipfile
import tempfile
import pandas as pd
import streamlit as st
from openpyxl import load_workbook
from PIL import Image
import pytesseract

# ====== KONFIGURASI STREAMLIT ======
st.set_page_config(
    page_title="Input Invoice Penjualan KSMT",
    page_icon="🌾",
    layout="wide",
)

st.markdown(
    """
    <h1 style='text-align: center; color: #f5f5f5;'>🌾 Input Invoice Penjualan KSMT</h1>
    <p style='text-align: center; color: #cccccc;'>Ekstraksi otomatis data dari foto invoice ke Excel</p>
    """,
    unsafe_allow_html=True,
)

# ====== PENGATURAN TEMA ======
st.markdown(
    """
    <style>
    body { background-color: #121212; color: #f5f5f5; }
    .stButton>button { background-color: #228B22; color: white; border-radius: 8px; padding: 8px 20px; }
    .stFileUploader { border: 1px solid #444; border-radius: 10px; padding: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ====== UPLOAD FILE ZIP ======
uploaded_zip = st.file_uploader("📦 Upload file ZIP berisi foto-foto invoice:", type=["zip"])

# Path template Excel
template_path = "Template.xlsx"

if uploaded_zip is not None:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Simpan zip ke folder sementara
        zip_path = os.path.join(temp_dir, "invoices.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_zip.read())

        # Ekstrak file ZIP
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        st.success("✅ File ZIP berhasil diekstrak. Mulai proses OCR...")

        # ====== PROSES OCR UNTUK SETIAP GAMBAR ======
        extracted_data = []
        for filename in os.listdir(temp_dir):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(temp_dir, filename)
                img = Image.open(img_path)

                # Ekstraksi teks dari gambar
                text = pytesseract.image_to_string(img, lang="ind")
                extracted_data.append({"File": filename, "Text": text})

        # Tampilkan hasil di Streamlit
        df = pd.DataFrame(extracted_data)
        st.write("### 🧾 Hasil Ekstraksi dari Semua Gambar")

