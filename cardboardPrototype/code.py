# SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Trinket Gemma Servo Control
# originally for Adafruit M0 boards, slightly modified for the feather m4 express (toomie's hw assignment - waving cat)
#code from: https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Trinket_Gemma_Servo_Control/code.py
# some variable names changed for my personal use

import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

# servo pin A1 
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
angle = 0

# potentiometer
knob = AnalogIn(board.A0)  # pot pin for servo control

def remap_range(value, left_min, left_max, right_min, right_max):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    left_span = left_max - left_min 
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    value_scaled = int(value - left_min) / int(left_span)

    # Convert the 0-1 range into a value in the right range.
    return int(right_min + (value_scaled * right_span))


while True:
    #translate the value from the knob to the servo
    angle = remap_range(knob.value, 0, 65535, 0, 180)
    my_servo.angle = angle
    
