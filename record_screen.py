import cv2
import numpy as np
import os
import pyautogui
import sys
import datetime
import time

def record_screen(file_name):
    date = str(datetime.date.today())
    output = date + "-" + file_name + ".mp4"

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
                print()
                break

        except Exception as e:
            print("Error", e)

    out.release()
    cv2.destroyAllWindows()


def main():
    if len(sys.argv) != 2:
        print("Add the name of the website! recorder.py <website name>")
        exit(1)

    time.sleep(3)

    print("Starting recording")
    record_screen(sys.argv[1])


if __name__ == '__main__':
    main()
