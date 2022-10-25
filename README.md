# video_edit
A library of utilities used to edit .mp4 video and srt (subtitle) files.

**movie_merge.py** - A utility used to merge all epoch named .mp4 files in a directory, into one single .mp4 file that is named for the day/date all files in the directory were created (as uploaded from Arlo).  A corresponding srt file is made so that the date/time of the video clip can be shown or turned off through viewer subtitle functionality.  
Uses: time, moviepy, os, datetime, pysrt, and conf (self-defined)

**conf.py** - Defines related folder structure information.

**media_info.py** - Incomplete

**one_thumbs.py** - Incomplete

**srt_create.py** - Utilty testing the pysrt library.
