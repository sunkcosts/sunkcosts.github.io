import base64
import streamlit as st
from pathlib import Path

APP_STATIC_DIR = Path(__file__).parent / "static"


@st.cache_data
def base64_of_bin(path: str) -> str:
    """
    Get base64 of binary file.

    Args:
        path (str): Path to file.

    Returns:
        str: b64 of file
    """
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_logo(
    path: str,
    link: str,
    top: str,
    bottom: str,
    left: str,
    right: str,
    height: str,
) -> None:
    """
    Add a logo to streamlit sidebar.
    """
    logo_b64 = base64_of_bin(path)
    markup = (
        "<a href='%s' target='_blank'><img src='data:image/png;base64,%s' style='z-index: 10000000; position: absolute; top: %s; bottom: %s; left: %s; right: %s; height: %s;' /></a>"
        % (
            link,
            logo_b64,
            top,
            bottom,
            left,
            right,
            height,
        )
    )
    st.markdown(
        markup,
        unsafe_allow_html=True,
    )


def configure_base_app():
    st.markdown(
        "<style>" + open(APP_STATIC_DIR / "theme.css").read() + "</style>",
        unsafe_allow_html=True,
    )
    add_logo(
        str(APP_STATIC_DIR / "logo.png"),
        link="https://www.github.io/sunkcosts/sunkcosts.github.io",
        top="44px",
        bottom="0px",
        left="auto",
        right="-60px",
        height="45px",
    )
