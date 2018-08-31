# https://picamera.readthedocs.io/en/release-1.13/recipes2.html#unencoded-image-capture-rgb-format

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.start_preview()
    time.sleep(2)
    camera.capture('image.data', 'rgb')
