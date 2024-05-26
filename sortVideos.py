from googleapiclient.discovery import build
import os

def get_youtube_video_urls(query, max_results=10):
    api_key = os.getenv("GOOGLEAPIKEY")  # Replace with your actual API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=max_results,
        type='video',
        relevanceLanguage='en',  # Filter by English language
        videoCaption='closedCaption'  # Filter by videos with closed captions
    )
    response = request.execute()

    video_urls = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_urls.append(video_url)

    return video_urls

# Example usage:
phone_model = 'Realme 9 pro plus 5g'
video_urls = get_youtube_video_urls(phone_model)
for url in video_urls:
    print(url)
