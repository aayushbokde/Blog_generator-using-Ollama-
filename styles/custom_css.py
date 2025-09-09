import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .generated-blog {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-size: 1rem;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    </style>
    """, unsafe_allow_html=True)
