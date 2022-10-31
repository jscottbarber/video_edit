import ffmpeg
import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from pprint import pprint

output_video = "D:\\Video\\Arlo\\2022\\2022-10\\2022-10-01.mp4"
#output_video = os.path.join(SAMPLE_OUTPUTS, "2022-10-22.mp4")
if os.path.exists(output_video):
  pprint(ffmpeg.probe(output_video)["streams"])
else:
  print("File Not Found.")