# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:02:06 2018
@author: sgb35
"""

from Project_routines import camera_routines as CR
from Project_routines import stepper_routines as MR
import time
import numpy as np

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
    
    
def centralise(reference_star):
    altitude_movement = (PIXEL_WIDTH/2) - reference_star[0]
    azimuth_movement = (PIXEL_LENGTH/2) - reference_star[1]

    if abs(altitude_movement) < 15:
        print('Alt Perf')
        pass
    elif altitude_movement < -15:
        while altitude_movement < -15:
            MR.altMotor.singleForward(int(-1*ALT_STEPS_PER_PIXEL*altitude_movement)+15)
            print('recalculating altitude...\n')
            reference_star = find_ref_star()
            altitude_movement = (PIXEL_WIDTH/2) - reference_star[0]
    elif altitude_movement > 15:
        while altitude_movement > 15:
            MR.altMotor.singleBackward(int(1*ALT_STEPS_PER_PIXEL*altitude_movement)+15)
            print('recalculating altidude...\n')
            reference_star = find_ref_star()
            altitude_movement = (PIXEL_WIDTH/2) - reference_star[0]
    
    if abs(azimuth_movement) < 15:
        pass
    elif azimuth_movement > 15:
        while azimuth_movement > 15:
            MR.azMotor.singleForward(int(3*ALT_STEPS_PER_PIXEL*azimuth_movement)+15)
            print('recalculating az...\n')
            reference_star = find_ref_star()
            azimuth_movement = (PIXEL_LENGTH/2) - reference_star[1]
    elif azimuth_movement < -15:
        while azimuth_movement < -15:
            MR.azMotor.singleBackward(int(-3*ALT_STEPS_PER_PIXEL*azimuth_movement)+15)
            print('recalculatingaz...\n')
            reference_star = find_ref_star()
            azimuth_movement = (PIXEL_LENGTH/2) - reference_star[1]
    print("DONE")
    CR.start_display()
            
            
##    #####CURRENTLY NO IDEA HOW THIS WORKS#####
##    from simple_pid import PID
##    pid = PID(1, 0.1, 0.05, setpoint=1)
##
##    # assume we have a system we want to control in controlled_system
##    v = controlled_system.update(0)
##    
##    while True:
##        # compute new ouput from the PID according to the systems current value
##        control = pid(v)
##    
##        # feed the PID output to the system and get its current value
##        v = controlled_system.update(control)
        
        
###TEST SECTION
        
#reference_star = find_ref_star()
#
#
#import PIL.Image
#img = PIL.Image.open('H:\FinalYearProject\single_star.jpg')
#img = np.array(img)
