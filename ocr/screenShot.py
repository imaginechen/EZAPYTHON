# Python 3.7.2
import keyboard # pip install keyboard
from PIL import ImageGrab   # pip install Pillow
from time import sleep
import sys
from baiduAI import BaiduAPI

def screenShot():
    '''used to save snapshot'''
    # screen shot start
    if keyboard.wait(hotkey='alt+a') == None:
        # screen shot end
        if keyboard.wait(hotkey='enter') == None:
            sleep(0.01)
            # copy the picture in the clipboard
            im = ImageGrab.grabclipboard()
            im.save('temp.png')

if __name__ == '__main__':

    baiduapi = BaiduAPI('password.ini')
    for _ in range(sys.maxsize):
        screenShot()
        print(baiduapi.picture2Text('temp.png'))