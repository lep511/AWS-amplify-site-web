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


@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map()

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


@app.route("/components")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        width=800,
        height=600,
    )

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                    {{ header|safe }}
                </head>
                <body>
                    <h1>Using components</h1>
                    {{ body_html|safe }}
                    <script>
                        {{ script|safe }}
                    </script>
                </body>
            </html>
        """,
        header=header,
        body_html=body_html,
        script=script,
    )


df = pd.read_csv('https://ckan.montevideo.gub.uy/dataset/159475cc-6584-48d3-961c-b6fa71e14cba/resource/fd845194-4cc7-43ea-bc06-00bbfb26f6f4/download/bprumd85rjyqcuqprxpplw.csv')
st.write(len(df))



age = st.slider('How old are you?', 0, 130, 25)

st.write(df.head(age))

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10*age, 20*age, 30*age, 40*age],
}))



st.write("I'm ", age, 'years old')

if __name__ == "__main__":
    app.run(debug=True)
