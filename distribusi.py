import streamlit as st
import pandas as pd

st.set_page_config(page_title="Google Sheets Loader Otomatis", layout="wide")

st.title("📄 Google Sheets Loader (Otomatis)")
st.write("Data diambil otomatis dari Google Sheets Anda tanpa tombol.")

# Google Sheet Anda
sheet_id = "1M395nIYCKa3euENuHc6E8fUeg-8Jfe0i"
sheet_name = "RESULT ST"   # Ubah jika sheet name berbeda

# URL CSV
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Load otomatis
try:
    df = pd.read_csv(url)
    st.success("Data berhasil dimuat otomatis dari Google Sheets!")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error("Gagal memuat data otomatis.")
    st.error(e)
