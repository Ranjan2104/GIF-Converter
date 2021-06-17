# Amresh Ranjan.

from moviepy.editor import *

clip = VideoFileClip("vedio.mp4")

# getting only 3 first seconds from video
clip = clip.subclip(0, 3)

# save the video clip as gif
clip.write_gif("mygif.gif")

print("Gif conversion is done!")
