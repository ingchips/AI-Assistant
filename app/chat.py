import streamlit as st
from chatonline import *

st.set_page_config(
    page_title="INGCHIPS AI-Assistant",
    page_icon="🧊",
)

st.title("INGCHIPS AI-Assistant")

pre_run()

if 'llm' not in st.session_state:
    start_page()
else:
    chat_page()