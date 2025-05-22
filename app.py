import streamlit as st

# Judul Aplikasi
st.title("Aplikasi Multi Menu")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Soal", "Hasil"])

# Konten berdasarkan menu
if menu == "Beranda":
    st.header("Selamat Datang di Aplikasi")
    st.write("Ini adalah halaman Beranda.")

elif menu == "Soal":
    st.header("Lembar Soal")
    soal = st.radio("Apa ibu kota Indonesia?", ["Jakarta", "Bandung", "Surabaya"])
    if st.button("Kirim Jawaban"):
        if soal == "Jakarta":
            st.success("Jawaban Benar!")
        else:
            st.error("Jawaban Salah.")

elif menu == "Hasil":
    st.header("Rekap Hasil")
    st.write("Belum ada hasil untuk ditampilkan.")
