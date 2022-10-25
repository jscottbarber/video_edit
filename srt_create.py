from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
import pysrt

# input_srt = os.path.join(SAMPLE_INPUTS, 'srt_input.srt')
output_srt = os.path.join(SAMPLE_OUTPUTS, 'srt_output.srt')
# subs = pysrt.open(input_srt, encoding='UTF-8')
# print(len(subs))
# for sub in subs:
  # pysrt.SubRipItem = sub
  # print(sub)
  # print(f'Start: {sub.start}')
  # print(f'End: {sub.end}')
  # print(f'Text: {sub.text}')
  # print(f'Index: {sub.index}')
  # print(f'Position: {sub.position}')

file = pysrt.SubRipFile()
sub = pysrt.SubRipItem(1, start='00:02:04,000', end='00:02:08,000', text="Hello World!")
file.append(sub)
file.save(output_srt, encoding='UTF-8')
# subs.save(output_srt, encoding='UTF-8')