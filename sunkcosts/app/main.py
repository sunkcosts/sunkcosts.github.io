import numpy as np
import streamlit as st
from pathlib import Path
from sunkcosts.app.config import configure_base_app

st.set_page_config(
    layout="wide",
    page_title="Sunk Costs Model",
    page_icon="🌊",
    initial_sidebar_state="expanded",
)

configure_base_app()
