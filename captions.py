from youtube_transcript_api import YouTubeTranscriptApi

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
print("Captions:")
print(captions)
