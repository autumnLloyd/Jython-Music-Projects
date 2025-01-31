# technologyRelationshipsScoundscape.py
# Author: Autumn R Lloyd
# Email: lloydar@g.cofc.edu
# Class: FYSE Comp Music Art
# Assignment: Homework 3
# Due Date: October 24, 2022
# Purpose: This program creates a soundscape meant to describe the role technology plays in unhealthy relationships

# appleTextNotif from : https://www.youtube.com/watch?v=AiMbf0ovXT4
# discordCall from : https://www.youtube.com/watch?v=HhdJmCnGteU
# discordNotif from : https://soundbuttons.net/discord-notification-sound
# phoneBuzz from : https://freesound.org/people/AnthonyRamirez/sounds/455413/
# outgoingCall from : https://freesound.org/people/tack00/sounds/401592/
# snapchatCall from : https://www.youtube.com/watch?v=yR8GrRamYiA

# importing data from music library
from music import *

# importing audio samples
appleTextNotif = AudioSample("applenotif.wav")
discordCall    = AudioSample("disccall.wav")
discordNotif   = AudioSample("discnotif.wav")
phoneBuzz      = AudioSample("phonebuzz.wav")
outgoingCall   = AudioSample("phonecall.wav")
snapchatCall   = AudioSample("snaptone.wav")

# creating empty score 
soundscape = Score("The Role Tech Plays in Unhealthy Relationships", 60)

# creating empty phrases, start time in seconds
appleTextPhrase        = Phrase(0.0)
discordCallPhrase      = Phrase(35.0)
discordNotifPhrase     = Phrase(12.0)
phoneBuzzPhrase        = Phrase(1.0)
outgoingCallPhrase     = Phrase(20.0)
snapchatCallPhrase     = Phrase(3.0)
appleTextClosingPhrase = Phrase(62.0)

# creating empty parts
appleTextPart        = Part(0, 0)
discordCallPart      = Part(1, 1)
discordNotifPart     = Part(2, 2)
phoneBuzzPart        = Part(3, 3)
outgoingCallPart     = Part(4, 4)
snapchatCallPart     = Part(5, 5)
appleTextClosingPart = Part(6, 6)

# adding notelists to phrases
# choosing to display timing in seconds rather than use
# presets such as notes because this is a soundscape
# and not a musical piece
##### single apple notification, grabs attention for interest curve
appleTextPhrase.addNoteList([A4], [2.0], [127])
##### phone buzz loop
phoneBuzzPhrase.addNoteList([A4], [1.0], [30], [.5], [1.0])
Mod.cycle(phoneBuzzPhrase, 59)
Mod.crescendo(phoneBuzzPhrase, 1.0, 60.0, 10, 127)
##### snapchat loop
snapchatCallPhrase.addNoteList([A4, REST], [2.0, 0.25], [127, 127])
Mod.cycle(snapchatCallPhrase, 49)
Mod.fadeIn(snapchatCallPhrase, 10)
##### discord notifications at varying intervals
discordNotifPhrase.addNoteList([A4, REST, A4, REST], [1.0, 4.0, 1.0, 2.0], [50, 127, 127, 127])
Mod.cycle(discordNotifPhrase, 24)
##### more phone buzzing
outgoingCallPhrase.addNoteList([A4, REST], [2.0, 4.0])
Mod.cycle(outgoingCallPhrase, 12)
##### discord call
discordCallPhrase.addNoteList([A4, REST], [5.0, 1.0], [80, 100])
Mod.cycle(discordCallPhrase, 7)
Mod.crescendo(discordCallPhrase, 35, 60, 10, 127)
##### second apple text, shows the cyclical nature of toxicity
appleTextClosingPhrase.addNoteList([A4], [2.0], [127])

# adding phrases to parts
appleTextPart.addPhrase(appleTextPhrase)
discordCallPart.addPhrase(discordCallPhrase)
discordNotifPart.addPhrase(discordNotifPhrase)
phoneBuzzPart.addPhrase(phoneBuzzPhrase)
outgoingCallPart.addPhrase(outgoingCallPhrase)
snapchatCallPart.addPhrase(snapchatCallPhrase)
appleTextClosingPart.addPhrase(appleTextClosingPhrase)

# adding parts to score
soundscape.addPart(appleTextPart)
soundscape.addPart(discordCallPart)
soundscape.addPart(discordNotifPart)
soundscape.addPart(phoneBuzzPart)
soundscape.addPart(outgoingCallPart)
soundscape.addPart(snapchatCallPart)
soundscape.addPart(appleTextClosingPart)

# tweaking volume
Mod.normalize(soundscape)

# debugging, helps me see where things end 
print (appleTextPhrase.getEndTime())
print (phoneBuzzPhrase.getEndTime())
print (snapchatCallPhrase.getEndTime())
print (discordNotifPhrase.getEndTime())
print (outgoingCallPhrase.getEndTime())
print (discordCallPhrase.getEndTime())
print (appleTextClosingPhrase.getEndTime())
print (soundscape.getEndTime())

# playing sounds
Play.audio(soundscape, [appleTextNotif, discordCall, discordNotif, phoneBuzz, outgoingCall, snapchatCall, appleTextNotif])