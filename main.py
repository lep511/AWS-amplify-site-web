import folium
import streamlit as st

from streamlit_folium import st_folium

m = folium.Map(location=CENTER_START, zoom_start=8)
fg = folium.FeatureGroup(name="Markers")
for marker in st.session_state["markers"]:
    fg.add_child(marker)

st_folium(
    m,
    center=st.session_state["center"],
    zoom=st.session_state["zoom"],
    key="new",
    feature_group_to_add=fg,
    height=400,
    width=700,
)
