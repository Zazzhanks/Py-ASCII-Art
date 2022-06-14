import moviepy.editor as mpe
import cv2
import numpy as np
import os
import natsort

def make_video():
  main_dir = os.getcwd()
  os.chdir('images/ascii_images')
  
  # choose codec according to format needed
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  
  video = cv2.VideoWriter('video.mp4', fourcc, 24, (3072, 1728))
  # Alternative solution but doesn't work on linux for some reason 
  # file_names = sorted(os.listdir())
  # file_names.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
  # print(file_names)

  for j in natsort.natsorted(os.listdir()):
      img = cv2.imread(j)
      video.write(img)
  
  cv2.destroyAllWindows()
  video.release()
  
  #Combines audio
  os.chdir(main_dir)
  my_clip = mpe.VideoFileClip('images/ascii_images/video.mp4')
  audio_background = mpe.AudioFileClip(f"audio/{os.listdir('audio')[1]}")
  final_clip = my_clip.set_audio(audio_background)
  final_clip.write_videofile('ascii_video/ascii_video.mp4',fps=60)
  print('done...')

