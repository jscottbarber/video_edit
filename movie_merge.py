import time
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import os
import datetime
import pysrt

def srt_format_timestamp(sec_duration):
  """Converts a number of seconds to an 00:00:00,000 (Hours:Minutes:Seconds,000) format"""
  return time.strftime("%H:%M:%S,000", time.gmtime(sec_duration))

this_dir = os.listdir(SAMPLE_INPUTS)
directory = {}

# Identify all .mp4 files in SAMPLE_INPUTS directory and add those filenames to a hashmap, key = epoch_string, Value = full path
for root, dirs, files in os.walk(SAMPLE_INPUTS):
  for fname in files:
    if fname.endswith("mp4"):
      filepath = os.path.join(root, fname)
      try:
        key = fname.replace(".mp4", "")
      except:
        key = None
      if key != None:
        directory[key] = filepath

#Prepare to loop through directory to create srt file
srt_file = pysrt.SubRipFile()  #Instantiate a SubRipFile object

running_video_duration = 0.0 #End SRT index in seconds
srt_entry_num = 0  #SRT file entry number

#Itterate through all files in the input directory
#For the sake of the output filename, this assumes all files in the folder are clips from the same day
for epoch_str in sorted(directory.keys()):
  #add 1 millisecond to the previous loop's duration as this loop's starting point in seconds, used for Start SRT index
  video_clip_start = running_video_duration + .001  

 #increment SRT entry index
  srt_entry_num+=1

  #Load a video clip from a file in the directory
  filepath = directory[epoch_str]
  clip = VideoFileClip(filepath) 

  ms_duration = clip.duration
  print(f"Processing file: {epoch_str} - Duration: {ms_duration}")
  #increment the total video duration
  running_video_duration += ms_duration

  #Convert the epoch string to a date and time
  ts = datetime.datetime.fromtimestamp(float(epoch_str)/1000)
  #Set SRT text to formatted date string
  srt_text = ts.strftime('%a %Y-%m-%d %I:%M %p')  
  
  #define output srt file name
  srt_filename = ts.strftime('%Y-%m-%d') + '.srt'
 
  #Create SRT entry and append it to the SRT file
  srt_start_time = srt_format_timestamp(video_clip_start)
  srt_end_time = srt_format_timestamp(running_video_duration)
  sub_rip = pysrt.SubRipItem(srt_entry_num, start=srt_start_time, end=srt_end_time, text=srt_text)
  srt_file.append(sub_rip)

#create and save the SRT file
print("Writing SRT File.")
srt_filepath = os.path.join(SAMPLE_OUTPUTS, srt_filename)
srt_file.save(srt_filepath, encoding='UTF-8')

#Prepare to loop through directory to create video file
clip_list = []  #List (collection) of all clips being concatinated

#Itterate through all files in the input directory
#For the sake of the output filename, this assumes all files in the folder are clips from the same day
for epoch_str in sorted(directory.keys()):

  #Load a video clip from a file in the directory
  filepath = directory[epoch_str]
  clip = VideoFileClip(filepath) 

  ms_duration = clip.duration
  print(f"Processing file: {epoch_str} - Duration: {ms_duration}")

  #Convert the epoch string to a date and time
  ts = datetime.datetime.fromtimestamp(float(epoch_str)/1000)
  
  #define output video and srt file names
  video_filename = ts.strftime('%Y-%m-%d') + '.mp4'

  #append the current video clip to the list and append a 1 second fadeout effect to the end
  clip_list.append(VideoFileClip(filepath).fx(vfx.fadeout, 1))

#Takes all clips found in the directory and adds them on one clip
result_clip = concatenate_videoclips(clip_list)

#Uses the last filenames from the loop to define the file names
video_filepath = os.path.join(SAMPLE_OUTPUTS, video_filename)

#creates the composite video file
print("Writing Video File.")
result_clip.write_videofile(video_filepath)
