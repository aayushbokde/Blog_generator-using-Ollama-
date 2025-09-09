import streamlit as st
from utils.history_utils import load_history

def render_sidebar():
    st.sidebar.header("⚙️ Configuration")
    model = st.sidebar.selectbox("Select Model", ["llama2:7b", "llama2:13b"])

    st.sidebar.header("📝 History")
    history = load_history()

    if history:
        for item in history[::-1]:  # latest first
            with st.sidebar.expander(item["topic"]):
                st.caption(f"**Audience:** {item['audience']}")
                st.caption(f"**Tone:** {item['tone']}")
                st.caption(f"**Words:** {item['word_count']}")
                st.caption(f"**Time:** {item['timestamp']}")
                st.text(item["content"][:200] + "...")
    else:
        st.sidebar.info("No history yet. Generate a blog to see history here.")

    return {"model": model}, history
