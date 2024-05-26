from pytube import YouTube

url = "https://www.youtube.com/watch?v=AxV0_1Y4zl0"

yt = YouTube(url)
caption = yt.captions['a.en']
print(caption.xml_captions)