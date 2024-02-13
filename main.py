#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import mozgas2


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
# motorok kezelése
jm = Motor(Port.B)
bm = Motor(Port.C)
#robot DriveBase(jm, bm, 56, 130)

# szenzorok
us = UltrasonicSensor(Port.S4)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)
gs = GyroSensor(Port.S2)

# robot irányítása
#robot.drive(100,0) #egyenesen megy

#robot.drive(0, 180) #forduljon 90 fokot
#wait(500)           #várjon amíg megtörténik a forgás

#robot.stop(Stop.Brake) #satufékes megállás
#2. ora 02.13.
# Motor kezelés
'''robot = DriveBase(jm, bm, 56, 132)
robot.straight(1000)
robot.drive(5000,0)
wait(1)
robot.straight(-1000)
wait(1)
robot.turn(-90)


mozgas2.foprogram()'''



# Write your program here.
ev3.speaker.beep()