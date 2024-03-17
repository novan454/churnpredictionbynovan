import pickle
import streamlit as st

model = pickle.load(open('Churn_Prediction.sav', 'rb'))
# Judul aplikasi
st.title('Customer Churn Prediction')
deskripsi_model = """
### Deskripsi Model Machine Learning

Customer Churn Prediction sebuah machine learning yang untuk perusahaan telekomunikasi dalam memprediski akankan pelanggannya akan melakukan churn atau tidak. Dimana jika hasilnya 1 merupakan ya (Churn) dan 0 adalah tidak (Tidak Churn), 

Model ini menggunakan Logistik Regression dengan nilai akurasi 1.0. Meskipun sempurna, bukan berarti semua prediksi yang dilakukan akan 100% benar, akan tetap dapat dijadikan referensi pertimbangan berdasarkan perhitungan ilmiah

Kemudian, Model ini menggunakan berbagai fitur seperti panjang akun, paket internasional, paket voicemail, jumlah pesan voicemail, total menit panggilan harian, total panggilan harian, total biaya harian, dan sebagainya.

"""

# Menampilkan deskripsi model machine learning
st.markdown(deskripsi_model)

# Membagi layar menjadi 4 kolom
kolom1, kolom2, kolom3, kolom4 = st.columns(4)

# Kolom 1
with kolom1:
    panjang_akun = st.number_input('Panjang Akun', min_value=0, key='kolom1_panjang_akun')
    paket_internasional = st.number_input('Paket Internasional', min_value=0, key='kolom1_paket_internasional')
    paket_voicemail = st.number_input('Paket Voicemail', min_value=0, key='kolom1_paket_voicemail')
    jumlah_pesan_voicemail = st.number_input('Jumlah Pesan Voicemail', min_value=0, key='kolom1_jumlah_pesan_voicemail')

# Kolom 2
with kolom2:
    total_menit_harian = st.number_input('Total Menit Harian', min_value=0, key='kolom2_total_menit_harian')
    total_panggilan_harian = st.number_input('Total Panggilan Harian', min_value=0, key='kolom2_total_panggilan_harian')
    total_biaya_harian = st.number_input('Total Biaya Harian', min_value=0, key='kolom2_total_biaya_harian')
    total_menit_malam = st.number_input('Total Menit Malam', min_value=0, key='kolom2_total_menit_malam')

# Kolom 3
with kolom3:
    total_panggilan_malam = st.number_input('Total Panggilan Malam', min_value=0, key='kolom3_total_panggilan_malam')
    total_biaya_malam = st.number_input('Total Biaya Malam', min_value=0, key='kolom3_total_biaya_malam')
    total_menit_internasional = st.number_input('Total Menit Internasional', min_value=0, key='kolom3_total_menit_internasional')
    total_panggilan_internasional = st.number_input('Total Panggilan Internasional', min_value=0, key='kolom3_total_panggilan_internasional')

# Kolom 4
with kolom4:
    total_intl_minutes = st.number_input('Total Menit Internasional', min_value=0, key='kolom4_total_intl_minutes')
    total_intl_calls = st.number_input('Total Panggilan Internasional', min_value=0, key='kolom4_total_intl_calls')
    total_intl_charge = st.number_input('Total Biaya Internasional', min_value=0, key='kolom4_total_intl_charge')
    jumlah_panggilan_layanan_pelanggan = st.number_input('Jumlah Panggilan Layanan Pelanggan', min_value=0, key='kolom4_jumlah_panggilan_layanan_pelanggan')

# Penjelasan untuk 0 dan 1
st.write("0 = Tidak dan 1 = Ya")

if st.button('Prediksi Churn'):
    predict = model.predict(
        [[panjang_akun, paket_internasional, paket_voicemail, jumlah_pesan_voicemail, total_menit_harian, total_panggilan_harian, total_biaya_harian, total_menit_malam, total_panggilan_malam, total_biaya_malam, total_menit_internasional, total_panggilan_internasional, total_biaya_malam, total_intl_minutes, total_intl_calls, total_intl_charge, jumlah_panggilan_layanan_pelanggan]]
    )
    st.write('Prediksi Churn: ', predict)
