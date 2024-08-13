from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
import jsonFormatllm
import json

def get_youtube_video_urls(query, max_results=10):
    api_key = os.getenv('GOOGLEAPIKEY')  # Replace with your actual API key
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
    return video_urls, video_info_list

def get_captions(video_id, language_code='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_phone_review(phone_model, max_videos):
  video_urls, video_info_list = get_youtube_video_urls(phone_model,max_videos)
  print(video_urls)

  captionsList = []
  for url in video_urls:
    video_id = url.split('v=')[1]
    caption = get_captions(video_id, language_code='en')
    captionsList.append(caption)
    print('generated')

    # Generate phone review prompt
    text_prompt = f"""
        You are a professional reviewer and your task is to summarize the reviews of a phone model based on the captions from the top 5 YouTube review videos. Here are the captions from the videos:

        Video 1: {captionsList[0]}
        Video 2: {captionsList[1]}
        Video 3: {captionsList[2]}
        Video 4: {captionsList[3]}
        Video 5: {captionsList[4]}

    Please write an overall review of the phone, summarizing the main points discussed in these videos. Your review should include:

    1. A brief introduction about the phone.
    2. A summary of the key features and performance aspects, highlighting the pros and cons.
    3. Citations in parentheses after each point indicating which video(s) the point was mentioned in (e.g., (1), (2), (3), etc.).

    Ensure the review is concise, well-structured, and clearly references the videos for each point made. Here is an example format for the review:

    ### Review of Phone_Name:

    The Phone_Name has been reviewed extensively, with a variety of opinions across different aspects.

    **Camera Quality**:
    - The camera hardware is excellent, providing sharp and detailed photos. However, the software seems to lag behind, causing occasional issues with color accuracy and processing speed (3).
    - Several reviewers praised the low-light performance of the camera, noting that it captures clear and bright images even in poor lighting conditions (1, 4).

    **Battery Life**:
    - The battery life is impressive, lasting well over a day with moderate use (2).
    - Some reviewers mentioned that heavy gaming or video streaming can drain the battery faster than expected (5).

    **Performance**:
    - The phone's performance is top-notch, handling multitasking and demanding applications with ease (1, 2, 4).
    - There were a few mentions of occasional stutters when switching between apps quickly (3).

    **Build Quality**:
    - The build quality is solid, with a premium feel and durable materials used throughout (2, 5).
    - A couple of reviewers pointed out that the phone is slightly heavier than its competitors (4).

    **Display**:
    - The display is vibrant and bright, making it great for media consumption (1, 3).
    - However, some found the display to be overly saturated in certain conditions (5).

    Overall, the Phone_Name is a strong contender in its market segment, offering a blend of high-quality hardware and impressive performance, though there are areas where it could improve, particularly in software optimization (3).

    **Pros**
    **Cons**

    Please ensure your review is well-organized and clearly references the videos for each point made.
        """

  # Configure and use large language model (replace with your API key)
  GEMMA_API=os.getenv("GEMINISTUDIOKEY")
  genai.configure(api_key=GEMMA_API)
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(text_prompt)

  return response.text, video_info_list

# Example usage (assuming GOOGLEAPIKEY and GEMINISTUDIOKEY are set as environment variables)
phone_model = 'Samsung S24 Ultra'
review, video_info_list = get_phone_review(phone_model,10)
ordered = jsonFormatllm.format_llm_review(review, video_info_list)
print(review, ordered)
