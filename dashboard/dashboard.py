import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
china_df = pd.read_csv('china_df.csv')

# Judul dan deskripsi aplikasi
st.title('Dashboard Kualitas Udara di China')
st.subheader('Analisis kualitas udara di beberapa stasiun')
st.markdown("""
Dashboard ini menampilkan tren kualitas udara di beberapa stasiun di China, dengan fokus
pada polutan seperti PM2.5, PM10, SO2, NO2, dan O3. Data berasal dari beberapa stasiun pemantauan.
""")

# Widget untuk memilih pertanyaan
question = st.radio(
    "Pilih Pertanyaan:",
    ('Tren Kualitas Udara di Stasiun', 'Perbandingan Kualitas Udara di Dua Stasiun (2016)')
)

if question == 'Tren Kualitas Udara di Stasiun':
    # Hanya tampilkan pilihan stasiun jika pertanyaan yang dipilih adalah tren kualitas udara
    station_option = st.selectbox("Pilih Stasiun:", china_df['station'].unique())
    
    # Filter data untuk stasiun yang dipilih
    station_df = china_df[china_df['station'] == station_option]

    # Pertanyaan 1: Tren kualitas udara di stasiun yang dipilih
    st.write(f"Menampilkan tren kualitas udara di {station_option}")
    
    # Mengelompokkan data berdasarkan tahun
    station_byyear = station_df.groupby('year').mean(numeric_only=True)

    # Membuat plot tren polutan
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(station_byyear['PM2.5'], label='PM2.5')
    plt.plot(station_byyear['PM10'], label='PM10')
    plt.plot(station_byyear['SO2'], label='SO2')
    plt.plot(station_byyear['NO2'], label='NO2')
    plt.plot(station_byyear['O3'], label='O3')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi Polutan')
    plt.title(f'Tren Kualitas Udara di {station_option}')
    plt.legend()
    st.pyplot(fig)

elif question == 'Perbandingan Kualitas Udara di Dua Stasiun (2016)':
    # Tampilkan pilihan dua stasiun untuk perbandingan
    station_1 = st.selectbox("Pilih Stasiun Pertama:", china_df['station'].unique(), index=0)
    station_2 = st.selectbox("Pilih Stasiun Kedua:", china_df['station'].unique(), index=1)
    
    # Filter data untuk kedua stasiun yang dipilih
    china_2016 = china_df[china_df['year'] == 2016]
    station_1_df = china_2016[china_2016['station'] == station_1]
    station_2_df = china_2016[china_2016['station'] == station_2]

    # Mengelompokkan data berdasarkan bulan
    station_1_bymonth = station_1_df.groupby('month').mean(numeric_only=True)
    station_2_bymonth = station_2_df.groupby('month').mean(numeric_only=True)

    # Plot perbandingan PM2.5
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(station_1_bymonth['PM2.5'], label=station_1)
    plt.plot(station_2_bymonth['PM2.5'], label=station_2)
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi PM2.5')
    plt.title(f'Perbandingan Konsentrasi PM2.5 di {station_1} dan {station_2} (2016)')
    plt.legend()
    st.pyplot(fig)

      # Plot perbandingan PM2.5
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(station_1_bymonth['PM10'], label=station_1)
    plt.plot(station_2_bymonth['PM10'], label=station_2)
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi PM10')
    plt.title(f'Perbandingan Konsentrasi PM10 di {station_1} dan {station_2} (2016)')
    plt.legend()
    st.pyplot(fig)

# Tambahkan footer
st.markdown('Tes Dashboard by Fatimatuz Zahra')
