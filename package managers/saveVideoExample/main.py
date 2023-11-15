from pytube import YouTube

video_url = "https://youtu.be/SBu5tSdmaHA?si=nd5l0VvxpocunYk0"
try:
    yt = YouTube(video_url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path)
    print("Скачивание завершено")
except Exception as e:
    print(f"Произошла ошибка: {e}")