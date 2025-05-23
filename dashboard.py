import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title("Estimasi Harga Mobil Toyota Bekas")

year = st.number_input("Input tahun mobil: ")
mileage = st.number_input("Input jarak tempuh mobil: ")
tax = st.number_input("Input pajak mobil: ")
mpg = st.number_input("Input konsumsi BBM mobil: ")
engineSize = st.number_input("Input ukuran mesin mobil: ")

predict = ''

if (st.button("Estimasi harga")):
  predict = model.predict(
    [[year, mileage, tax, mpg, engineSize]]
  )
  st.write("Estimasi harga mobil toyota bekas: ", predict, "pounds")
  st.write("Estimasi harga mobil toyota bekas: ", predict * 19000, "rupiah")
