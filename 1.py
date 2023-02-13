from moviepy.editor import VideoFileClip

video = VideoFileClip('C:\\Users\\Stark\\Downloads\\Meditation\\40.mp4')
audio = video.audio
audio.write_audiofile('C:\\Users\\Stark\\Downloads\\Meditation\\40.mp3')