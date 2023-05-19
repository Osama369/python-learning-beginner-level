import youtube_dl

# Ask for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTubeDL object
ydl = youtube_dl.YoutubeDL({})

try:
    # Extract video information
    video_info = ydl.extract_info(video_url, download=False)

    # Check if captions are available
    if 'automatic_captions' in video_info or 'captions' in video_info:
        print("This video has captions.")
    else:
        print("This video does not have captions.")

except youtube_dl.DownloadError:
    print("Invalid YouTube video URL.")
