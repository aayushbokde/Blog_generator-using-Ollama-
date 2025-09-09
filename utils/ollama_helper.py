import subprocess

def generate_with_ollama(prompt, model="llama2:7b"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,  # prompt is a string
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"⚠️ Error generating text: {str(e)}"
