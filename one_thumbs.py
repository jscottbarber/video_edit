from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *

source_path = os.path.join(SAMPLE_INPUTS, '1665581712727.mp4')

clip = VideoFileClip(source_path)
print(clip.reader.fps)  # frames per second
print(clip.reader.nframes) 
print(clip.duration)  # seconds

duration = clip.duration  # clip.reader.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
  print(f"frame at {i} seconds")
  frame = clip.get_frame(i)
  print(frame)  # np.array numby array # inference
