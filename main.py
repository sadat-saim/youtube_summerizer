import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json

# Streamlit app title
st.title("📺 YouTube Video Summarizer with AI")

# Input field for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:")


def get_auto_generated_captions(video_url):
    """Extracts auto-generated captions from a YouTube video."""
    try:
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        else:
            return "Invalid YouTube URL"

        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en'])
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"Error: {str(e)}"


def generate_summary(captions):
    """Sends captions to the Ollama API for summarization."""
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "deepseek-r1:1.5b",
        "prompt": f'You are given the transcription of a YouTube video below. Summarize the main contents.\n\n"{captions}"\n\nSummary:',
        "stream": True
    }

    with requests.post(url, headers=headers, json=data, stream=True) as response:
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line)
                    yield data["response"]  # Stream response
                except json.JSONDecodeError:
                    continue


if st.button("Summarize Video"):
    if video_url:
        st.subheader("🎬 Extracted Captions:")
        captions = get_auto_generated_captions(video_url)

        if captions.startswith("Error"):
            st.error(captions)
        else:
            st.write(captions[:500] + "...")  # Show a preview

            st.subheader("📝 AI-Generated Summary:")
            summary_text = st.empty()  # Placeholder for streaming text
            summary = ""

            for chunk in generate_summary(captions):
                summary += chunk  # Append streamed text
                summary_text.write(summary)  # Update in real-time
    else:
        st.warning("Please enter a valid YouTube URL.")
