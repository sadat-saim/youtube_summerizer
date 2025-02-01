from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json


def get_auto_generated_captions(video_url):
    # Extract video ID from the URL
    video_id = video_url.split("v=")[1].split("&")[0]  # Handles standard URLs
    if "youtu.be/" in video_url:
        # Handles shortened URLs
        video_id = video_url.split("youtu.be/")[1].split("?")[0]

    try:
        # Fetch auto-generated captions (specify languages if needed, e.g., ['en'])
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en'])
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"Error: {str(e)}"


video_url = "https://www.youtube.com/watch?v=ewXANEIC8pY&ab_channel=IanWootten"
captions = get_auto_generated_captions(video_url)


url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "deepseek-r1:1.5b",  # Change this to your model
    "prompt": f"""You are given the transcription of a youtube video in the paragraph below. You need to summerize the main
    contents of the video.
    "{captions}"
    """,
    "stream": True  # Enable streaming
}

# Send request with streaming enabled
with requests.post(url, headers=headers, json=data, stream=True) as response:
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line)  # Parse JSON response
                # Print only response text
                print(data["response"], end="", flush=True)
            except json.JSONDecodeError:
                continue  # Skip malformed lines
