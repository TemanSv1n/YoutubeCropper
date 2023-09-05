from moviepy.editor import *
#import pytube
import yt_dlp
import random

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
def Download(link: str):
    file_name = f"vid-{random.randint(1000, 9999)}.mp4"
    ydl_opts = {
        'format': 'best',  # Select the best available format
        'outtmpl': "downloads/" + file_name,  # Output file template
        'quiet': False,  # Suppress output messages
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        okay = False
        try:
            ydl.download([link])
            okay = True
            file_name = "downloads/" + file_name
        except:
            print("ooga booga!")
            return "-1"
        if okay:
            print(file_name)
            return file_name
        else:
            print("ooga booga!")
            return "-1"

def VideoCrop(file: str, start: float, stop: float):
    #file = "downloads/vid-4607.mp4"
    print(file)
    clip = VideoFileClip(file)
    file_name_2 = f"{file}-cut{random.randint(10,99)}.mp4"
    clip2 = clip.subclip(start, stop)
    clip2.write_videofile(file_name_2)

    clip.close()
    try:
        clip2.close()
    except:
        print("oops")
    print(f"{file_name_2} is ready!")
    return file_name_2
