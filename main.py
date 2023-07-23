import streamlit as st
import pandas as pd
import folium 

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
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
