from moviepy.editor import *
import sys

assert(len(sys.argv)==3 or len(sys.argv)==4), 'Expected arguments: <path/to/gif.gif> <path/to/song.mp3> <BPM (OPTIONAL)>'

mygif = VideoFileClip(sys.argv[1], audio=False)
audio = AudioFileClip(sys.argv[2])
bpm = int(sys.argv[3]) if len(sys.argv)==4 else None

if bpm is not None:
    seconds_per_beat = 60/bpm
    # compute the new duration of the gif accroding to the BPM and create a new gif with appropriate speed
    new_gif_duration = seconds_per_beat * round(mygif.duration / seconds_per_beat)
    mygif2 = mygif.fx(vfx.accel_decel, new_gif_duration, abruptness=0)
    print('original gif duration: ',  mygif.duration)
    print('new gif duration ',  mygif2.duration)

else:
    mygif2 = mygif

#mygif2 = mygif2.fx(vfx.make_loopable, cross=0.1)
mygif3 = mygif2.fx(vfx.loop, duration =audio.duration) # loop the gif for the song's duration
mygif4 = mygif3.set_audio(audio) # add the audio to the video
mygif4.write_videofile("result.mp4", codec='mpeg4',fps=30,bitrate='3500k', audio_codec='aac', audio_bitrate='320k') # export the resulting video as mp4