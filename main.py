import argparse
import os
import subprocess
import sys
import time
import cv2
import pygame
import numpy as np
from PIL import Image

def parse_arguments():
    parser = argparse.ArgumentParser(description='ASCII video player')
    parser.add_argument('-f', '--file', required=True, help='Video file path')
    parser.add_argument('-c', '--color', action='store_true', help='Enable color output')
    return parser.parse_args()

def play_audio(video_file):
    def audio_thread():
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(video_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except:
            pass
    
    import threading
    thread = threading.Thread(target=audio_thread)
    thread.daemon = True
    thread.start()

def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size()
        return rows, columns
    except OSError:
        return 25, 80

def resize_frame(frame, new_width):
    height, width = frame.shape[:2]
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return cv2.resize(frame, (new_width, new_height))

def frame_to_ascii(frame, color_frame=None):
    chars = " .:-=+*#%@"[::-1]
    
    if len(frame.shape) == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = frame
        
    normalized = gray / 255
    
    ascii_frame = ""
    for i, row in enumerate(normalized):
        for j, pixel in enumerate(row):
            char = chars[int(pixel * (len(chars) - 1))]
            
            if color_frame is not None:
                b, g, r = color_frame[i, j]
                ascii_frame += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            else:
                ascii_frame += char
        ascii_frame += "\n"
    
    return ascii_frame

def main():
    args = parse_arguments()
    
    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found")
        sys.exit(1)

    term_rows, term_cols = get_terminal_size()
    width = min(term_cols, 120)
    
    play_audio(args.file)
    
    cap = cv2.VideoCapture(args.file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if fps > 0 else 0.03
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            if args.color:
                color_resized = resize_frame(frame, width)
                gray_resized = cv2.cvtColor(color_resized, cv2.COLOR_BGR2GRAY)
                ascii_art = frame_to_ascii(gray_resized, color_resized)
            else:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                resized = resize_frame(gray, width)
                ascii_art = frame_to_ascii(resized)
            
            sys.stdout.write("\033[H\033[J")
            sys.stdout.write(ascii_art)
            sys.stdout.flush()
            
            time.sleep(delay)
            
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        try:
            pygame.mixer.quit()
        except:
            pass
        sys.stdout.write("\033[0m")
        sys.stdout.flush()

if __name__ == "__main__":
    main()