# video_edit
A library of utilities used to edit .mp4 video and srt (subtitle) files.

**movie_merge.py** - A utility used to merge all epoch named .mp4 files in a directory, into one single .mp4 file that is named for the day/date all files in the directory were created (as downloaded from Arlo).  A corresponding srt file is made so that the date/time of the video clip can be shown or turned off through viewer subtitle functionality.  
Uses: time, moviepy, os, datetime, pysrt, and conf (self-defined)

**conf.py** - Defines related folder structure information.

**create_folders.py** - A utility used to create folders under D:\Video\Arlo\[current_year] for each day of the current month (format: D:\Video\Arlo\2022\2022-10-31), skipping folders that may already exist.  These folders are used when manually downloading security videos from Arlo's website.

**media_info.py** - Incomplete

**one_thumbs.py** - Incomplete

**srt_create.py** - Utilty testing the pysrt library.
