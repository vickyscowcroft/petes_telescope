# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:52:46 2018
@author: sgb35
"""
from io import BytesIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
from time import sleep
import numpy as np
##from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.feature import register_translation
from math import sqrt
##import matplotlib.pyplot as plt


camera = PiCamera()
camera.start_preview()
sleep(10)
camera.stop_preview()
CAMERA_RESOLUTION = (1024,768)
CAMERA_FRAMERATE = 24


def capture_image_to_file(filepath, camera=camera):
    '''
    Function to capture immediate image to a file
    
    Input : filepath - string
            path where image is to be stored
    Returns: None
    '''
    try:
        camera=PiCamera()
    except picamera.exc.PiCameraMMALError:
        print("Camera already running")
    with camera:
        camera.resolution = CAMERA_RESOLUTION
        camera.capture(filepath)
##    camera.stop_preview()
##    
def start_display(position_size=(100,100,256,192), camera=camera):
    try:
        camera=PiCamera()
    except picamera.exc.PiCameraMMALError:
        print("Camera already running")
    #Allows the user to define the size of the preview window and its location on the screen 'x,y,w,h'
    camera.start_preview(fullscreen = False, window = position_size)

def stop_display():
    camera.stop_preview()

def grey_image():
    image = image_to_array()
    im_gr = rgb2gray(image)
    im_gr[im_gr < 0.3] = 0
    return im_gr
    
def image_to_array(camera=camera): 
    '''
    Function to capture image to a numpy array
    
    Input : None
    Returns: array containing image
    '''
    try:
        camera=PiCamera()
    except picamera.exc.PiCameraMMALError:
        print("Camera already running")
          
    with camera:
        camera.resolution = CAMERA_RESOLUTION
        camera.framerate = CAMERA_FRAMERATE
        sleep(2)
        output = np.empty((768*1024*3), dtype = np.uint8)
        camera.capture(output,'rgb')
        output = output.reshape((768,1024,3))
        return output
    
def find_star_locations(imageArray):
    '''
    Function to locate bright spots on an image
    
    Input : RGB array of image
    Returns: numpy array of bright spots y,x,r
    '''
    image_grey = rgb2gray(imageArray)
    blobs = blob_log(image_grey, max_sigma=30, num_sigma=10, threshold=.1)
    blobs[:, 2] = blobs[:, 2] * sqrt(2)
    return blobs
    


# =============================================================================
# test = find_star_locations(image)
# 
# 
# 
# 
# # Create an array representing a 1280x720 image of
# # a cross through the center of the display. The shape of
# # the array must be of the form (height, width, color)
# a = np.zeros((720, 1280, 3), dtype=np.uint8)
# a[360, :, :] = 0xff
# a[:, 640, :] = 0xff
# 
# ax[idx].imshow(image, interpolation='nearest')
# =============================================================================
def produce_overlay(camera=camera):
    with camera:
        camera.resolution = CAMERA_RESOLUTION
        camera.framerate = CAMERA_FRAMERATE
        camera.start_preview(fullscreen = False, window = position_size)
        current_image = image_to_array()
        stars_current = find_star_locations(current_image)
        # Add the overlay directly into layer 3 with transparency;
        # we can omit the size parameter of add_overlay as the
        # size is the same as the camera's resolution
        for blob in stars_current:
            y, x, r = blob
            c = plt.Circle((x, y), r, color='lime', linewidth=2, fill=False)
            o = camera.add_overlay(np.getbuffer(c), layer=3, alpha=64)
        try:
            # Wait indefinitely until the user terminates the script
            while True:
                time.sleep(1)
        finally:
            camera.remove_overlay(o)

def drift_amount(image1, image2):
    drift, error, diffphase = register_translation(image1, image2)
    print('{}, er - {}, diffphase - {}'.format(drift, error, diffphase))
    return drift

def check():
    print('hello')
# =============================================================================
# import PIL.Image
# img = PIL.Image.open('C:\Users\sgb35\Downloads\FirstPictureChimney_20181016.jpeg')
# exif_data = img._getexif()
# 
# from PIL import Image
# from PIL.ExifTags import TAGS
#  
# def get_exif(fn):
#     ret = {}
#     i = Image.open(fn)
#     info = i._getexif()
#     for tag, value in info.items():
#         decoded = TAGS.get(tag, tag)
#         ret[decoded] = value
#     return ret
# =============================================================================
