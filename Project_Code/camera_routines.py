# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:52:46 2018

@author: sgb35
"""
from io import BytesIO
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import numpy as np



CAMERA_RESOLUTION = (1024,768)
CAMERA_FRAMERATE = 24

def capture_image_to_file(filepath):
    '''
    Function to capture immediate image to a file
    
    Input : filepath - string
            path where image is to be stored
    Returns: None
    '''
    camera = PiCamera()
    camera.resolution = CAMERA_RESOLUTION
    camera.start_preview()
    
    sleep(2)
    camera.capture(filepath)
    
def start_display(position_size=(100,100,256,192)):
    camera = PiCamera()
    #Allows the user to define the size of the preview window and its location on the screen 'x,y,w,h'
    camera.start_preview(fullscreen = False, window = position_size)

def stop_display():
    camera.stop_preview()
    
def image_to_array(): 
    '''
    Function to capture image to a numpy array
    
    Input : None
    Returns: array containing image
    '''
    with PiCamera() as camera:
        camera.resolution = CAMERA_RESOLUTION
        camera.framerate = CAMERA_FRAMERATE
        sleep(2)
        output = np.empty((768,1024,3), dtype = np.uint8)
        camera.capture(output,'rgb')
        return output
    
