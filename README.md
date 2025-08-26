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

<img width="1372" height="660" alt="Preview" src="https://github.com/user-attachments/assets/66305e3f-46eb-4221-badb-5872a500b19f" />

# How it works

Each frame is processed by Open-CV

<img width="899" height="221" alt="VideoToASCII" src="https://github.com/user-attachments/assets/4f1a1005-1e9a-4297-8f50-f63d9b2e64fa" />

Next get the terminal X and Y size,
once we have the terminal size, we convert each frame into the same frame but in a lower resolution

<img width="810" height="347" alt="Simpsons" src="https://github.com/user-attachments/assets/75e55a5e-c31d-48ca-b242-009240df34c1" />

After conversion, we take the color of each pixel and convert it to ASCII based on the color intensity.

```chars = " .:-=+*#%@"```

0-255 RGB to ASCII.
And we get a ASCII frame

<img width="1094" height="716" alt="Frame" src="https://github.com/user-attachments/assets/dbe6e314-5691-4c81-bd3a-4b9872c548fa" />

# Creators

@PiaPsyker918
