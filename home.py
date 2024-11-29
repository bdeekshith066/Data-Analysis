import streamlit as st
import json
from streamlit_lottie import st_lottie

# Function to load Lottie animations from JSON files
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Set file paths for Lottie animations
animation1 = load_lottie_animation("assets/Animation1.json")
animation2 = load_lottie_animation("assets/Animation2.json")
animation3 = load_lottie_animation("assets/Animation3.json")
animation4 = load_lottie_animation("assets/Animation4.json")
animation5 = load_lottie_animation("assets/Animation5.json")
animation6 = load_lottie_animation("assets/Animation6.json")
animation7 = load_lottie_animation("assets/Animation7.json")
animation8 = load_lottie_animation("assets/Animation8.json")
animation9 = load_lottie_animation("assets/Animation9.json")

def app():
    # Set catchy title and subtitle
    st.title("Data Dynamics: Unveiling Hidden Patterns")
    st.write(" :orange[Discover the hidden story your data is trying to tell, unlocking powerful insights that drive smarter decisions and fuel future growth]")


    # Create a 3x3 grid layout with explicit columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st_lottie(animation1, height=250, key="animation1")
    with col2:
        st_lottie(animation7, height=250, key="animation2")
    with col3:
        st_lottie(animation6, height=250, key="animation3")
    
    st.write('')

    col4, col5, col6 = st.columns(3)
    with col4:
        st_lottie(animation2, height=250, key="animation4")
    with col5:
        st_lottie(animation3, height=250, key="animation5")
    with col6:
        st_lottie(animation4, height=250, key="animation6")

    st.write('')
    st.write('')

    col7, col8, col9 = st.columns(3)
    with col7:
        st_lottie(animation5, height=250, key="animation7")
    with col8:
        st_lottie(animation8, height=250, key="animation8")
    with col9:
        st_lottie(animation9, height=250, key="animation9")

    # Additional styling or padding if needed
    st.markdown("""
        <style>
            .css-1x8cf1d {padding-top: 1rem;}
            .css-1v3fvcr {padding-top: 1rem;}
        </style>
    """, unsafe_allow_html=True)
