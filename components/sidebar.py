import streamlit as st

def render_sidebar():
    st.sidebar.header("⚙️ Configuration")
    model = st.sidebar.selectbox("Select Model", ["llama2:7b", "llama2:13b"])
    
    st.sidebar.header("📝 History")
    history = []
    st.sidebar.info("Generated blogs will appear here in future.")

    return {"model": model}, history
