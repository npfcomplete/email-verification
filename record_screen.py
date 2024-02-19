import cv2
import numpy as np
import os
import pyautogui
import sys
import datatime
import time

def record_screen(file_name)
    date = process_time()
    output = date + file_name + ".mp4"

    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    height, width, channels = img.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    while("Record Screen"):
        try:
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)
            except KeyboardInterrupt:
                break

        out.release()
        cv2.destroyAllWindows()

def process_time():
    current_date = str(datetime.date.today()).split("-")
    return current_date[1] + "-" + current_date[2] + 
            "-" + currentdate[0] + "-"


def main():
    if len(sys.argv != 2):
        print("Add the name of the website! recorder.py <website name>")
        exit(1)

    time.sleep(3)

    record_screen(argv[1])


if __name__ == '__main__':
    main()
