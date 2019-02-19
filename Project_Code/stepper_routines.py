# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:50:55 2018
@author: sgb35
"""

from Adafruit_MotorHAT import Adafruit_MotorHAT

import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr = 0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

class Motor:
    def __init__(self, motorPort):
        self.motornumber = mh.getStepper(48, motorPort)    # 48 steps/rev, motor port selected
        self.motornumber.setSpeed(70)              # 70 standard (also 70rpm)

    def singleForward(self, numberSteps):
        print'{} single coil steps forward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

    def singleBackward(self, numberSteps):
        print'{} single coil steps backward'.format(numberSteps)    
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

    def doubleForward(self, numberSteps):
        print'{} double coil steps forward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

    def doubleBackward(self, numberSteps):
        print'{} double coil steps backward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

    def interleaveForward(self, numberSteps):
        print'{} interleaved coil steps forward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)

    def interleaveBackward(self, numberSteps):
        print'{} interleaved coil steps backward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

    def microForward(self, numberSteps):
        print'{} microsteps forward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

    def microBackward(self, numberSteps):
        print'{} microsteps backward'.format(numberSteps)
        self.motornumber.step(numberSteps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP) 
    
atexit.register(turnOffMotors)

altMotor = Motor(1)
azMotor = Motor(2)
