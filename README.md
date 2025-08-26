# ASCII-Console-Video
This is a program that analyzes a video using Open-CV and displays it as ASCII art.

<img width="1189" height="276" alt="Logo" src="https://github.com/user-attachments/assets/47b512d4-1c97-44fa-922c-ef9166ac824b" />

Video preview:
https://github.com/user-attachments/assets/850365d7-770a-455b-aeaf-09d36f484430

(There are gaps in the video when the script is being performed, but there are no gaps in real life.)

# Translations

-  Russian: 

# Requirements
* argparse
* os
* subprocess
* sys
* time
* cv2
* pygame
* numpy
* PIL

# Installation

1. Install the zip-file.
2. Open CMD and write.
```
pip install requements.txt
```
3. Download the .mp4 file.
4. Next step in "How to use".

# How to use

In CMD write
Windows
```
.\main.py -f video_file.mp4
```
Linux
```
$ ./main.py -f video_file.mp4
```

# Options
```-f``` - Specify the name of the file with the .mp4 extension. IT MUST BE LOCATED IN THE SAME DIRECTORY AS THE SCRIPT.
```-c``` - If the video has color, the console will display a color ASCII video.

![Uploading Preview.png…]()
