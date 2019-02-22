# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:02:06 2018
@author: sgb35
"""

from Project_routines import camera_routines_2 as CR
from Project_routines import stepper_routines as MR
import time
import numpy as np
from time import sleep

PIXEL_LENGTH = 1024
PIXEL_WIDTH = 768
ALT_STEPS_PER_PIXEL=1
AZ_STEPS_PER_PIXEL=1
STEP_PER_DEG = 720

#take current stream as image
def find_ref_star():
    current_image = CR.image_to_array()
    star_locations = CR.find_star_locations(current_image)
    star_locations = star_locations[star_locations[:,2].argsort()]
    return(star_locations[-1])



def star_tracking():
    try:
        while (True):
            centralise(find_ref_star())
            time.sleep(20)
    except KeyboardInterrupt:
        print('interrupted!')


def centralise(image_1, image_2):
    shift = CR.drift_amount(image_1, image_2)
    
    altitude_movement = shift[0]
    azimuth_movement = shift[1]

    if abs(altitude_movement) < 5:
        print('Alt Perf')
        pass
    elif altitude_movement < 0:
        while altitude_movement < -5:
            MR.altMotor.singleForward(int(-4*ALT_STEPS_PER_PIXEL*altitude_movement))
            print('recalculating altitude...\n')
            image_2 = CR.grey_image()
            shift = CR.drift_amount(image_1, image_2)
            altitude_movement = shift[0]
    elif altitude_movement > 0:
        while altitude_movement > 5:
            MR.altMotor.singleBackward(int(4*ALT_STEPS_PER_PIXEL*altitude_movement))
            print('recalculating altidude...\n')
            image_2 = CR.grey_image()
            shift = CR.drift_amount(image_1, image_2)
            altitude_movement = shift[0]
##            image_2 = image_1
    
    if abs(azimuth_movement) < 5:
        pass
    elif azimuth_movement < 0:
        while azimuth_movement < -5:
            MR.azMotor.singleForward(int(-3*ALT_STEPS_PER_PIXEL*azimuth_movement))
            print('recalculating az...\n')
            image_2 = CR.grey_image()
            shift = CR.drift_amount(image_1, image_2)
            azimuth_movement = shift[1]
    elif azimuth_movement > 0:
        while azimuth_movement > 5:
            MR.azMotor.singleBackward(int(3*ALT_STEPS_PER_PIXEL*azimuth_movement))
            print('recalculating az...\n')
            image_2 = CR.grey_image()
            shift = CR.drift_amount(image_1, image_2)
            azimuth_movement = shift[1]
##            image_2 = image_1
    print("DONE")
    
def main():
    
    print('Welcome to Jon and Seb\'s star tracking program.\n')
    
    begin = raw_input('Would you like to begin tracking? - (Y/N)') 
    
    if begin != 'N':
        
        print('Please set the viewfinder so that the current sky is that to be tracked.\n')
        sleep(5)
        raw_input('When you are ready to begin tracking, press any key - ')
        
        ref_image = CR.grey_image()
        sleep(5)
        shifted_image = CR.grey_image()
        
        x = 1
        while x < 2:
            try:
                centralise(ref_image, shifted_image)
                sleep(5)
                shifted_image = CR.grey_image()
                
            except KeyboardInterrupt:
                print('Tracking terminated')
                x = 3
                
                
main()
    
