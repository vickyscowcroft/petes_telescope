#  https://picamera.readthedocs.io/en/release-1.13/recipes2.html#capturing-to-a-numpy-array

import time
import picamera
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.framerate = 24
    time.sleep(2)
    output = np.empty((112 * 128 * 3,), dtype=np.uint8)
    camera.capture(output, 'rgb')
    output = output.reshape((112, 128, 3))
    output = output[:100, :100, :]


## TO DO - send this output to a fits file
