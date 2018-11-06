# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:02:06 2018

@author: sgb35
"""

import camera_routines as cam
import stepper_routines as stepper
import numpy as np

PIXEL_LENGTH = 1066
PIXEL_WIDTH = 800
ALT_STEPS_PER_PIXEL=1
AZ_STEPS_PER_PIXEL=1

#take current stream as image
def find_ref_star():
    current_image = cam.image_to_array()
    star_locations = cam.find_star_locations(current_image)
    star_locations = star_locations[star_locations[:,2].argsort()]
    return(star_locations[-1])



def star_tracking():
    centralise(find_ref_star())
    
    
def centralise(reference_star):
    altitude_movement = (PIXEL_LENGTH/2) - reference_star[1]
    azimuth_movement = (PIXEL_WIDTH/2) - reference_star[0]

    if altitude_movement == 0:
        pass
    elif altitude_movement < 0:
        while altitude_movement < 0:
            altMotor.stepper.singleForward(ALT_STEPS_PER_PIXEL*altitude_movement)
            reference_star = find_ref_star()
            altitude_movement = (PIXEL_LENGTH/2) - reference_star[1]
    elif altitude_movement > 0:
        while altitude_movement < 0:
            altMotor.stepper.singleBackward(ALT_STEPS_PER_PIXEL*altitude_movement)
            reference_star = find_ref_star()
            altitude_movement = (PIXEL_LENGTH/2) - reference_star[1]
    
    if azimuth_movement == 0:
        pass
    elif azimuth_movement < 0:
        while azimuth_movement < 0:
            azMotor.stepper.singleForward(ALT_STEPS_PER_PIXEL*azimuth_movement)
            reference_star = find_ref_star()
            azimuth_movement = (PIXEL_LENGTH/2) - reference_star[1]
    elif azimuth_movement > 0:
        while azimuth_movement < 0:
            azMotor.stepper.singleBackward(ALT_STEPS_PER_PIXEL*azimuth_movement)
            reference_star = find_ref_star()
            azimuth_movement = (PIXEL_LENGTH/2) - reference_star[1]
         
            
            
    #####CURRENTLY NO IDEA HOW THIS WORKS#####
    from simple_pid import PID
    pid = PID(1, 0.1, 0.05, setpoint=1)

    # assume we have a system we want to control in controlled_system
    v = controlled_system.update(0)
    
    while True:
        # compute new ouput from the PID according to the systems current value
        control = pid(v)
    
        # feed the PID output to the system and get its current value
        v = controlled_system.update(control)
        
        
###TEST SECTION
        
reference_star = find_ref_star()


import PIL.Image
img = PIL.Image.open('H:\FinalYearProject\single_star.jpg')
img = np.array(img)
