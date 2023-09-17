### Assignment 1: RGB Hello World
# LED blinking to the beat of a snippet from Newjeans' song 'Super Shy'

## [Demo Video](https://youtube.com/shorts/iHTNNCPa9mk?feature=share)

## Concept
For this assignment, we were tasked with telling a story or creating an experience by animating the single RGB LED that is on our adafruit Feather. I thought it would be interesting to create an experience in which I program the LED to match the beats in a song. I decided to go with NewJeans' 'Super Shy' and used bright colors to represent the beats of the song. I chose to use the first approx. 30 seconds of the song because I felt that the intro beat and the first verse would look really cool on the LED. The colors I chose for the LED were influenced by the album cover of this song:

<img src= "https://i.scdn.co/image/ab67616d0000b2730744690248ef3ba7b776ea7b" width = "420">


## Highlights
I modified the [example code](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led)
 that we used for this assignment.
 
To start, I experimented with which color codes to choose to best match the cover and the vibe of the song, and I made variables to save these colors so I could easily use them in the code:
```
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
```

To start off the song, I made a little countdown with the LED so I know exactly when to press play on the song:
```
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
```
I really took my time listening to the song and getting the beats just right, and I split the lyrics in my code into parts to work on, and I added a short comment of which lyric corresponds to which line of code, like this:

```
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
```

## Reflection
I think the final result is quite fun and satisfying to watch! If I was to rework this code in the future, I'd add a speaker and connect the song to the code so I wouldn't need the countdown code. It was pretty hard pressing play at the right moment every time I wanted to run the code, so adding the snippet of the song into the code would make it so much easier to work with. There also may be an easier way to get the timing of the beats right, but I just did it by ear this time.


## Code
You can find the full code [here](https://github.com/oomie/desertmediaart/edit/main/exercise1/code.py)
