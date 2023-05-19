

# Path: app.py
from pytube import YouTube
  # pytube is a 
# use youtube video link

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link) 
print(yt.title)
# print(yt.thumbnail_url)

# first we check streeming of the video

videos = yt.streams.all()
#  # convert into list of all streaming of a video

video_list= list(enumerate(videos))
#  # now print all videos streams 
for i, j in video_list:

    print(f"{i} {j}")
#     # print all video streams with index number

# # input the option which streams to be  seleted
print("\n")
strm= int(input("enter your streaming index"))   

videos[strm].download()

print("successfully downloaded")



