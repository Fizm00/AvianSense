import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(
    page_title="AvianSense",
    page_icon="🦅",
    initial_sidebar_state="collapsed",
)

pages = ["Home", "Upload", "Gallery", "About", "Help", "Github"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "Avian_Sense.svg")
urls = {}
styles = {
    "nav": {
        "background-color": "#1a5f7a",
        "justify-content": "left",
        "height": "75px",
    },
    "img": {
        "padding-right": "50px",
        "height": "150px",
    },
    "span": {
        "color": "white",
        "padding": "25px",
    },
    "active": {
        "textdecoration": "underline",
        "color": "#7AB2D3",
        "font-weight": "normal",
        "padding": "25px",
    }
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.show_home,
    "Upload": pg.show_main,
    "Gallery": pg.show_gallery,
    "About": pg.show_about,
    "Help": pg.show_help,
    "Github": pg.show_github
}
go_to = functions.get(page)
if go_to:
    go_to()