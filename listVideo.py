from googleapiclient.discovery import build
import os
import json

def get_youtube_video_urls(query, max_results=5):
    api_key = os.getenv('GOOGLEAPIKEY')  # Replace with your actual API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=max_results,
        type='video'
    )
    response = request.execute()
    video_info_list = []
    for item in response['items']:
        snippet = item['snippet']
        video_info = {
        "title": snippet['title'],
        "author": snippet['channelTitle'],
        "videoId": item['id']['videoId']
        }
        video_info_list.append(video_info)
    print(json.dumps(video_info_list, indent=2))
    video_urls = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_urls.append(video_url)
    
    print(video_urls)

    return video_urls, video_info_list

# Example usage:
phone_model = 'Realme 9 pro plus 5g'
video_urls = get_youtube_video_urls(phone_model)
# for url in video_urls:
#     print(url)