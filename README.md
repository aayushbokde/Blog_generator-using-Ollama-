# 📝 Blog Generator using Ollama + LLaMA 2

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)  
[![Model](https://img.shields.io/badge/AI-LLaMA2-blue)](https://ollama.ai/)  
[![Python](https://img.shields.io/badge/Python-3.9+-yellow)](https://www.python.org/)  

A **Streamlit web application** powered by **Ollama** and **LLaMA 2** models to generate high-quality blogs.  
Easily customize **topic, audience, word count, and tone**, and keep track of generated blogs with an in-app history feature.  

---

## ✨ Features
✅ Generate blogs using **LLaMA 2 (7B / 13B)** models via Ollama  
✅ Customize blog **topic, audience, tone, and length**  
✅ Auto-save blog history in `history.json`  
✅ Sidebar with **blog history & previews**  
✅ Export blogs as `.txt` files  
✅ Clean, minimal UI with **custom CSS styling**  

---

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/)  
- **LLM Backend:** [Ollama](https://ollama.ai/) running **LLaMA 2** models locally  
- **Language:** Python 3.9+  

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```
git clone https://github.com/<your-username>/Blog_generator-using-Ollama-.git
cd Blog_generator-using-Ollama-
```
### 2️⃣ Install dependencies
```
pip install -r requirements.txt

```
### 3️⃣ Install Ollama

Download Ollama for your OS
Pull the required LLaMA 2 models:
ollama pull llama2:7b
ollama pull llama2:13b   # optional

### 4️⃣ Run the app
```
streamlit run app.py
```
### 📖 Usage


Enter a blog topic (e.g., AI in Healthcare)

Select the target audience (Researchers, Students, General Readers, etc.)

Adjust word count and tone

Click Generate Blog 🚀

Blog appears in the UI with an option to download

Sidebar shows your blog history


### 🔮 Future Enhancements


 Support PDF export

 Multi-language blog generation

### 👨‍💻 Author

```
Developed by Aayush Bokde
```


