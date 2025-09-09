import streamlit as st
from datetime import datetime

def render_blog(topic, content, audience, word_count, tone, history):
    st.success("✅ Blog generated successfully!")

    st.header("📄 Generated Blog")
    st.write(f"**Topic:** {topic}")
    st.write(f"**Audience:** {audience}")
    st.write(f"**Tone:** {tone}")
    st.write(f"**Target Word Count:** {word_count}")
    st.write(f"**Generated at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    st.markdown("---")
    st.markdown(content)

    # Download option
    st.download_button("📥 Download Blog", data=content, file_name=f"blog_{topic.replace(' ', '_')}.txt")
