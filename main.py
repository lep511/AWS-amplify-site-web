import streamlit as st
import pandas as pd
from flask import Flask, render_template_string

import folium

app = Flask(__name__)

@app.route("/")
def fullscreen():
    """Simple example of a fullscreen map."""
    m = folium.Map()
    return m.get_root().render()


m = folium.Map(location=[40.965, -5.664])

df = pd.read_csv('https://ckan.montevideo.gub.uy/dataset/159475cc-6584-48d3-961c-b6fa71e14cba/resource/fd845194-4cc7-43ea-bc06-00bbfb26f6f4/download/bprumd85rjyqcuqprxpplw.csv')
st.write(len(df))



age = st.slider('How old are you?', 0, 130, 25)

st.write(df.head(age))

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10*age, 20*age, 30*age, 40*age],
}))



st.write("I'm ", age, 'years old')
