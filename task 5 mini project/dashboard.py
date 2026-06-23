import streamlit as st
import pandas as pd

st.title("🌍 Smart Environment Monitoring Dashboard")

df = pd.read_csv("sensor_data.csv")

st.subheader("Current Sensor Readings")
st.dataframe(df)

st.subheader("Temperature")
st.metric("Temperature", f"{df['Temperature'][0]} °C")

st.subheader("Humidity")
st.metric("Humidity", f"{df['Humidity'][0]} %")

st.subheader("Motion")
st.write(df["Motion"][0])

st.subheader("Automation Status")

st.write("Fan:", df["Fan"][0])
st.write("Dehumidifier:", df["Dehumidifier"][0])
st.write("Alarm:", df["Alarm"][0])