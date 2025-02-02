# 🎥 YouTube Video Summarizer  

This is a simple Python application that uses **Streamlit** as a frontend to take a **YouTube video URL** as input and generate a **summary** of the video's content. The summarization is powered by the **DeepSeek-R1 1.5B** model, which runs locally using **Ollama**.  

## 🖥️ Preview
![preview](/screencapture-localhost-8501-2025-02-01-22_27_35.png)

## 🚀 Features  

- **📌 Simple & Intuitive UI** – Enter a YouTube URL and get a summarized version of the video.  
- **🤖 AI-Powered Summarization** – Uses `deepseek-r1:1.5b` for high-quality text summarization.  
- **⏳ Real-time Processing** – Captions are extracted and processed instantly.  
- **🖥️ Runs Locally** – No external API calls; everything runs on your machine using Ollama.  

---

## 🛠️ Installation & Setup  

### 1️⃣ Install Dependencies  

Ensure you have **Python 3.7+** installed, then install the required dependencies:  

```bash
pip install streamlit youtube-transcript-api requests
```

### 2️⃣ Install & Run Ollama  

1. Install **[Ollama](https://ollama.com/)** by following the official installation instructions.  
2. Download and start the **DeepSeek-R1 1.5B** model:  

   ```bash
   ollama run deepseek-r1:1.5b
   ```

3. Exit the interactive Ollama prompt by typing:  

   ```bash
   /bye
   ```

   ✅ *Make sure Ollama is running in the background while using the app!*  

### 3️⃣ Run the Streamlit App  

Start the application using:  

```bash
streamlit run main.py
```

Or alternatively:  

```bash
python -m streamlit run main.py
```

---

## 🔍 How It Works  

1. **User Input** – Enter a YouTube video URL in the Streamlit app.  
2. **Captions Extraction** – The app fetches auto-generated subtitles using `youtube-transcript-api`.  
3. **Summarization** – The transcript is sent to `deepseek-r1:1.5b`, which generates a summary.  
4. **Real-time Display** – The models generates a summary of the transcript.  

---

## 🤝 Contributing  

Want to improve this project? Contributions are welcome!  

- **Fork** the repo  
- **Create** a new branch  
- **Submit** a pull request 🚀  

For bug reports and feature requests, open an issue on **GitHub**.  
