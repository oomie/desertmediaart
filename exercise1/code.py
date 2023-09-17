# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
# modified code from the rgb hello world example


"""LED animation assignment: led blinking to the beat of Newjeans' song Super Shy """
# by toomie (fatima aljunaibi)

# COLOR REFERENCES
YELLOW = (255, 150, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 230)
PINK = (230, 50, 150)
LPINK = (255, 100, 100)
LBLUE = (50, 150, 255)
WHITE = (255,255,255)
OFF = (0,0,0)

import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 1


while True:

    #intro countdown
    led[0] = WHITE
    time.sleep(0.5)
    led[0] = OFF
    time.sleep(0.5)
    led[0] = WHITE
    time.sleep(0.5)
    led[0] = OFF
    time.sleep(0.5)
    led[0] = WHITE
    time.sleep(0.5)
    led[0] = OFF #i press play on spotify RIGHT at this point
    time.sleep(0.3)

    #intro beat pt 1
    led[0] = PURPLE
    time.sleep(1.3)
    led[0] = CYAN
    time.sleep(1.3)
    led[0] = PURPLE
    time.sleep(0.2)
    led[0] = CYAN
    time.sleep(0.2)
    led[0] = PURPLE
    time.sleep(0.2)
    led[0] = CYAN
    time.sleep(0.2)
    led[0] = LPINK
    time.sleep(1.2)
    led[0] = YELLOW
    time.sleep(2)

    #intro beat pt 2
    led[0] = PURPLE
    time.sleep(1.3)
    led[0] = CYAN
    time.sleep(1.1)
    led[0] = PURPLE
    time.sleep(0.2)
    led[0] = CYAN
    time.sleep(0.2)
    led[0] = PURPLE
    time.sleep(0.2)
    led[0] = CYAN
    time.sleep(0.2)
    led[0] = LPINK
    time.sleep(1.2)
    led[0] = LBLUE
    time.sleep(1.2)

    #START THE VERSE!
    led[0] = CYAN
    time.sleep(0.2)
    led[0] = PURPLE
    time.sleep(0.1)
    led[0] = CYAN
    time.sleep(0.05)
    led[0] = PURPLE
    time.sleep(0.05)
    led[0] = CYAN
    time.sleep(0.05)
    led[0] = PURPLE
    time.sleep(0.05)
    led[0] = CYAN
    time.sleep(0.05)
    led[0] = PURPLE
    time.sleep(0.05)
    led[0] = CYAN
    time.sleep(0.05)
    led[0] = PURPLE
    time.sleep(0.05)
    led[0] = LPINK
    time.sleep(0.1)

    #first verse: im super shyy -> make u mine
    led[0] = CYAN   #SU
    time.sleep(0.2)
    led[0] = PURPLE  #PER
    time.sleep(0.2)
    led[0] = LPINK    #SHY
    time.sleep(0.5)
    led[0] = CYAN  #SU
    time.sleep(0.2)
    led[0] = PURPLE    #PER
    time.sleep(0.2)
    led[0] = LPINK  #SHY
    time.sleep(0.5)
    led[0] = CYAN    #BUT
    time.sleep(0.2)
    led[0] = PURPLE  #WAIT
    time.sleep(0.2)
    led[0] = CYAN    #A
    time.sleep(0.2)
    led[0] = PURPLE  #MI
    time.sleep(0.2)
    led[0] = CYAN    #NUTE
    time.sleep(0.1)
    led[0] = PURPLE  #WHILE
    time.sleep(0.2)
    led[0] = CYAN    #I
    time.sleep(0.2)
    led[0] = PURPLE  #MAKE
    time.sleep(0.2)
    led[0] = CYAN    #U
    time.sleep(0.2)
    led[0] = LPINK  #MINE
    time.sleep(0.6)
    led[0] = PURPLE  #MAKE
    time.sleep(0.2)
    led[0] = CYAN    #U
    time.sleep(0.2)
    led[0] = LPINK  #MINE
    time.sleep(0.4)

    #VERSE PT 2 (tteollineun jigeumdo you're on my mind all the time)
    led[0] = CYAN    #tteol
    time.sleep(0.2)
    led[0] = PURPLE  #li
    time.sleep(0.2)
    led[0] = CYAN    #neun
    time.sleep(0.2)
    led[0] = PURPLE  #ji
    time.sleep(0.2)
    led[0] = CYAN    #geum
    time.sleep(0.2)
    led[0] = PURPLE  #do
    time.sleep(0.2)
    led[0] = CYAN    #ur
    time.sleep(0.2)
    led[0] = PURPLE  #on
    time.sleep(0.2)
    led[0] = CYAN    #my
    time.sleep(0.2)
    led[0] = LPINK   #mind
    time.sleep(0.5)
    led[0] = PURPLE  #all
    time.sleep(0.2)
    led[0] = CYAN    #the
    time.sleep(0.2)
    led[0] = LPINK   #time
    time.sleep(0.5)

    #final part (i wanna tell u but im super shyyy, super shyyy)
    led[0] = CYAN    #i
    time.sleep(0.2)
    led[0] = PURPLE  #wa
    time.sleep(0.2)
    led[0] = CYAN    #nna
    time.sleep(0.2)
    led[0] = PURPLE  #tell
    time.sleep(0.2)
    led[0] = CYAN    #u
    time.sleep(0.2)
    led[0] = PURPLE  #but
    time.sleep(0.2)
    led[0] = CYAN    #im
    time.sleep(0.25)
    led[0] = PURPLE  #su
    time.sleep(0.2)
    led[0] = CYAN    #per
    time.sleep(0.2)
    led[0] = PINK    #SHY
    time.sleep(0.3)
    led[0] = LPINK   #-YY : i used a lighter pink for this higher note
    time.sleep(0.9)

    led[0] = PURPLE  #su
    time.sleep(0.2)
    led[0] = CYAN    #per
    time.sleep(0.2)
    led[0] = PINK    #SHY
    time.sleep(0.3)
    led[0] = LPINK   #-YY
    time.sleep(1)
