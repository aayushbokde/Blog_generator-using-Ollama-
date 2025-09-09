import streamlit as st
from utils.ollama_helper import generate_with_ollama
from utils.prompts import build_prompt
from components.sidebar import render_sidebar
from components.blog_display import render_blog
from styles.custom_css import load_css

def main():
    st.set_page_config(page_title="LLaMA 2 Blog Generator", page_icon="✍️", layout="wide")
    load_css()

    st.title("🤖 LLaMA 2 Blog Generator")
    st.subheader("Generate high-quality blog content tailored to your audience using AI")

    # Sidebar
    config, history = render_sidebar()

    # Blog config inputs
    topic = st.text_area("Enter Blog Topic", placeholder="E.g., AI in Healthcare, Climate change...")
    audience = st.selectbox("Target Audience", ["Researchers", "Data Scientists", "Common People", "Students", "Business Professionals"])
    word_count = st.slider("Word Count", 100, 2000, 500, 50)
    tone = st.select_slider("Tone", options=["Formal", "Professional", "Conversational", "Casual", "Friendly"], value="Professional")

    if st.button("🚀 Generate Blog"):
        if not topic:
            st.error("Please enter a topic first!")
        else:
            with st.spinner("Generating blog..."):
                prompt = build_prompt(topic, audience, word_count, tone)
                blog_content = generate_with_ollama(prompt, config["model"])
                render_blog(topic, blog_content, audience, word_count, tone, history)

if __name__ == "__main__":
    main()
