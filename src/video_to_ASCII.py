import cv2
from moviepy.editor import *
import os 
from picture_to_video import make_video
import time


def get_file_name():
    video_name = os.listdir('video')[0]
    print(video_name)
    return str(video_name)

def get_audio():
    video_name  = get_file_name()
    video = VideoFileClip(f"video/{video_name}")
    audio = video.audio
    audio.write_audiofile(f"audio/{video_name.split('.')[0]}.mp3")

def get_frames():
    
    run = 0
    video_name  = get_file_name()
    vidcap = cv2.VideoCapture(f"video/{video_name}")
    success, image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)      
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps

    for i in range(frame_count):
        run += 1
        
        cv2.imwrite("images/video_images/image_%d.jpg" % run, image)    
        success, image = vidcap.read()
        print('Saved image ', run)


if __name__  == '__main__':
    start_time = time.time()
    get_frames()
    from ascii_ import main
    main()
    make_video()
    print("--- %s seconds ---" % (time.time() - start_time))