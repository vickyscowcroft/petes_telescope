from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
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
        self.motornumber = mh.getStepper(200, motorPort)    # 200 steps/rev, motor port selected
        self.motornumber.setSpeed(3)              # 30 RPM

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

#Step Type Guide
#Single Steps - this is the simplest type of stepping, and uses the least power.
#It uses a single coil to 'hold' the motor in place.
#
#Double Steps - this is also fairly simple, except instead of a single coil,
#it has two coils on at once.
#For example, instead of just coil #1 on, you would have coil #1 and #2 on at once.
#This uses more power (approx 2x) but is stronger than single stepping (by maybe 25%).
#
#Interleaved Steps - this is a mix of Single and Double stepping,
#where we use single steps interleaved with double.
#It has a little more strength than single stepping, and about 50% more power.
#Tt makes your motor appear to have 2x as many steps, for a smoother transition between steps.
#
#Microstepping - this is where we use a mix of single stepping with Pulse Width Modulation
#to slowly transition between steps.
#It's slower than single stepping but has much higher precision. 
