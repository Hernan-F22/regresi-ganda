import pickle
import streamlit as st
import os

# Aplikasi Streamlit
st.title('Prediksi Kalori')

# Load the trained KNN model
model_path = 'regression_model.pkl'  # Ganti dengan jalur yang benar jika perlu
print("Memuat model dari:", os.path.abspath(model_path))

try:
    with open(model_path, 'rb') as model_file:
        knn = pickle.load(model_file)
except FileNotFoundError:
    print("File model tidak ditemukan. Pastikan jalur dan nama file benar.")
except Exception as e:
    print(f"Terjadi kesalahan saat memuat model: {e}")

# Form input data
st.header('Masukan Data')
umur = st.number_input('Umur', min_value=25, max_value=55)
bb = st.number_input('Berat Badan (BB)', min_value=60, max_value=95)
tb = st.number_input('Tinggi Badan (TB)', min_value=155, max_value=180)
olahraga = st.number_input('Durasi Olahraga (menit)', min_value=20, max_value=90)

# Tombol prediksi
if st.button('Prediksi'):
    # Membuat model dari file pickle
    loaded_model = pickle.load(open('regression_model.pkl', 'rb'))

    # Melakukan prediksi
    input_data = [[umur, bb, tb, olahraga]]
    prediction = loaded_model.predict(input_data)

    # Menampilkan hasil prediksi
    st.header('Hasil Prediksi')
    st.write(f'Kalori yang diperkirakan: {prediction[0]:.2f}')
    
