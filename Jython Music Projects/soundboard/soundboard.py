# soundboard.py
#
# Author:  Autumn Rose Lloyd
# Email:   lloydar@g.cofc.edu
# Class:   FYSE 180
# Assignment: Homework #5
# Due Date:  28 November 2022 
#
# Purpose: This is a simple soundboard that simulates a thunderstorm.
#
# Icon images were digitally drawn by me in Open Canvas.
#
# Sources for my audio files can be found in the text document attached in this folder.
#

from gui import *
from music import *

# importing sound files
birdsong  = AudioSample ("birdsongedited.wav")
heavyRain = AudioSample ("heavyrainedited.wav")
lightning = AudioSample ("lighteningedited.wav")
thunder   = AudioSample ("thunderedited.wav")
wind      = AudioSample ("windedited.wav")

# standardizing color scheme
darkBlue = Color(45,54,87)
darkNavy = Color(39,51,63)
teal     = Color(47,206,210)
white    = Color(255, 255, 255)

# importing and resizing images
birdsongIcon  = Icon("birdsongIcon.png", 100, 100)
lightningIcon = Icon("lightningIcon.png", 100, 100)
thunderIcon   = Icon("thunderIcon.png", 100, 100)
windIcon      = Icon("windIcon.png", 100, 100)

# creating variables
pushNote = Note(A4, WN)

# creating display
soundboardDisplay = Display("thunderstorm soundboard", 450, 350, 150, 50, darkNavy)

# establishing functions for when buttons and sliders are used

def heavyRainVolume(volume):
   global heavyRain
   heavyRain.setVolume(volume)
   
def birdsongPush(value):
   global birdsong, pushNote
   Play.audio(pushNote, [birdsong])
   
def lightPush(value):
   global lightning, pushNote
   Play.audio(pushNote, [lightning])
   
def thunderPush(value):
   global thunder, pushNote
   Play.audio(pushNote, [thunder])
   
def windPush(value):
   global wind, pushNote
   Play.audio(pushNote, [wind])

# visual design
birdsongPushElement = Push(150, 50, 250, 150, birdsongPush, darkBlue, teal, darkBlue, 3)
lightPushElement    = Push(300, 50, 400, 150, lightPush, darkBlue, teal, darkBlue, 3)
thunderPushElement  = Push(150, 200, 250, 300, thunderPush, darkBlue, teal, darkBlue, 3)
windPushElement     = Push(300, 200, 400, 300, windPush, darkBlue, teal, darkBlue, 3)

heavyRainVolumeElement = VFader(50, 50, 75, 250, 0, 127, 0, heavyRainVolume, teal, darkBlue, darkBlue, 3)
heavyRainVolumeLabel   = Label("Rain Volume")
heavyRainVolumeLabel.setForegroundColor(white)

# adding elements to the display
soundboardDisplay.add(birdsongPushElement)
soundboardDisplay.add(lightPushElement)
soundboardDisplay.add(thunderPushElement)
soundboardDisplay.add(windPushElement)
soundboardDisplay.add(heavyRainVolumeElement)

# adding Icons and Labels
soundboardDisplay.add(birdsongIcon, 150, 50)
soundboardDisplay.add(lightningIcon, 300, 50)
soundboardDisplay.add(thunderIcon, 150, 200)
soundboardDisplay.add(windIcon, 300, 200)
soundboardDisplay.add(heavyRainVolumeLabel, 34, 265)

# ambient rain
heavyRain.loop()