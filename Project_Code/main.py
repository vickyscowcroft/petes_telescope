# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:02:06 2018

@author: sgb35
"""

import camera_routines as cam
import stepper_routines as stepper

PIXEL_LENGTH = 500
PIXEL WIDTH = 500

#take current stream as image
capture_image_to_file(current_image)
star_locations = cam.find_star_locations(current_image)
star_locations = star_locations[star_locations[:,2].argsort()]
reference_star = star_locations[-1]


def star_tracking():
    
    altitude_movement = (PIXEL_LENGTH/2) - reference_star[1]
    azimuth_movement = (PIXEL_WIDTH/2) - reference_star[0]

    if altitude_movement == 0:
        pass
    elif altitude_movement < 0:
        while altitude_movement < 0:
            altMotor.stepper.singleForward(100)
        