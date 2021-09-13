import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fill the MASK",
                   page_icon="💡")

''' # Fill the GAP'''
st.text("Write something")
st.write("To know more about this app, visit [**GitHub**](https://github.com/srajanseth84/FTG)")


@st.cache(allow_output_mutation=True)
def load_model():
    model = pipeline("fill-mask", model="bert-base-uncased")
    return model


model_load_state = st.text('Loading Model...')
model = load_model()

# Notify the reader that the data was successfully loaded.
model_load_state.text('Loading Model...done!')


input = st.text_area('Write something', height=30)
button = st.button("Know fill")


with st.spinner("Finding suitable word"):
    if button and input:
        answers = model(input)
        st.write(answers)

st.markdown("Created by **Srajan Seth**")
st.markdown(body="""
<th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
<th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
""", unsafe_allow_html=True)