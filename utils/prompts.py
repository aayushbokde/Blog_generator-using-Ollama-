def build_prompt(topic, audience, word_count, tone):
    return f"""You are an expert blog writer. Write a {word_count}-word blog about "{topic}" for {audience}.
Tone: {tone}.
Use clear structure with introduction, main sections, and conclusion.
Adjust complexity based on the audience.
"""
