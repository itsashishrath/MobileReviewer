from youtube_transcript_api import YouTubeTranscriptApi
import os

def get_captions(video_id, language_code='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage:
youtube_url = "https://www.youtube.com/watch?v=AxV0_1Y4zl0"
video_id = youtube_url.split('v=')[1]
captions = get_captions(video_id, language_code='en')

import google.generativeai as genai

GEMMA_API=os.getenv("GEMINISTUDIOKEY")
genai.configure(api_key=GEMMA_API)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(captions)

print(response.text)
