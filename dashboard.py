import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_day = pd.read_csv('day.csv')

df_day['season'] = df_day['season'].replace({
    1: 'Semi', 
    2: 'Panas', 
    3: 'Gugur', 
    4: 'Dingin'
})

df_day['weathersit'] = df_day['weathersit'].replace({
    1: 'Cerah', 
    2: 'Berkabut', 
    3: 'Gerimis', 
    4: 'Hujan Deras'
})

st.title('Dashboard Bike Sharing')

st.header("Grafik Bike Sharing")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h5>1. Grafik Berdasarkan Musim:</h5>", unsafe_allow_html=True)

    plt.figure(figsize=(10,5))
    sns.barplot(
        x = "season",
        y = "cnt",
        data=df_day.sort_values(by="season", ascending=False),
        palette="coolwarm",
        errorbar=None
    )
    plt.title("Total Penyewaan Berdasarkan Musim", fontsize=15)
    plt.xlabel("Musim", fontsize=12)
    plt.ylabel("Jumlah", fontsize=12)
    st.pyplot(plt)

    st.markdown("<p style='text-align: justify;'>Pada grafik di atas, penyewaan sepeda tertinggi terjadi pada musim Gugur, dengan total penyewaan melebihi 5000 unit.</p>", unsafe_allow_html=True)


with col2:
    st.markdown("<h5>2. Grafik Berdasarkan Cuaca:</h5>", unsafe_allow_html=True)

    plt.figure(figsize=(10,5))
    sns.barplot(
        x = "weathersit",
        y = "cnt",
        data=df_day.sort_values(by="weathersit", ascending=False),
        palette="coolwarm",
        errorbar=None
    )
    plt.title("Total Penyewaan Berdasarkan Cuaca", fontsize=15)
    plt.xlabel("Cuaca", fontsize=12)
    plt.ylabel("Jumlah", fontsize=12)
    st.pyplot(plt)

    st.markdown("<p style='text-align: justify;'>Pada grafik di atas, penyewaan sepeda tertinggi terjadi pada cuaca Cerah, dengan total penyewaan hampir menyentuh 5000 unit.</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title('Dashboard Bike Sharing')
    st.write('Ini merupakan dashboard untuk melihat traffic penyewaan sepeda berdasarkan beberapa faktor, seperti musim dan cuaca')