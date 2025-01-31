# snakeGui.1.py
#
# Author:  Autumn Rose Lloyd
# Email:   lloydar@g.cofc.edu
# Class:   CITA 284 / CSCI 299
# Assignment: Final Project
# Due Date:  28 April 2023
#
# Purpose: This program generates a controller for a game of multiplayer snake.
#
# Input:   Users use their mouse to select their snake and the direction they would like it to move in
#
# Output:  Six snakes move, grow, and compete to become the longest snake or the last one standing.
#
# All graphics are hand drawn and belong to me.
#
# Game Rules: 
#          1. When a snake overlaps an apple, it grows by one segment.
#          2. If a snake touches itself or another snake it dies
#          3. A snake may not turn back on itself, it may only move in 3 directions at any time.
#          4. If a snake hits a wall, it moves two segments backwards.
#

from gui import *
from osc import *

# get the IP from the user
IPaddress = input("Please enter the host's IP Address:")

# update gui
def refreshColors():
   global d, up, down, left, right
   
   # remove old buttons
   d.remove(up)
   d.remove(down)
   d.remove(left)
   d.remove(right)
   
   d.remove(upArrow)
   d.remove(downArrow)
   d.remove(leftArrow)
   d.remove(rightArrow)
   
   # recolor
   up    = Push(350, 150, 550, 250, moveUp, buttonForeground, buttonBackground, Color.WHITE, 0)
   down  = Push(350, 450, 550, 550, moveDown, buttonForeground, buttonBackground, Color.WHITE, 0)
   left  = Push(200, 300, 400, 400, moveLeft, buttonForeground, buttonBackground, Color.WHITE, 0)
   right = Push(500, 300, 700, 400, moveRight, buttonForeground, buttonBackground, Color.WHITE, 0)

   # redraw
   d.add(up)
   d.add(down)
   d.add(left)
   d.add(right)
   
   d.add(upArrow, 350, 150)
   d.add(downArrow, 350, 450)
   d.add(rightArrow, 500, 300)
   d.add(leftArrow, 200, 300)
   
# button functions
def setPlayer1(pushed):
   global buttonForeground, p1Foreground, buttonBackground, p1Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p1Foreground
   buttonBackground = p1Background
   refreshColors()
   # change osc base message
   base = "/player1/"
def setPlayer2(pushed):
   global buttonForeground, p2Foreground, buttonBackground, p2Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p2Foreground
   buttonBackground = p2Background
   refreshColors()
   # change osc base message
   base = "/player2/"
def setPlayer3(pushed):
   global buttonForeground, p3Foreground, buttonBackground, p3Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p3Foreground
   buttonBackground = p3Background
   refreshColors()
   # change osc base message
   base = "/player3/"
def setPlayer4(pushed):
   global buttonForeground, p4Foreground, buttonBackground, p4Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p4Foreground
   buttonBackground = p4Background
   refreshColors()
   # change osc base message
   base = "/player4/"
def setPlayer5(pushed):
   global buttonForeground, p5Foreground, buttonBackground, p5Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p5Foreground
   buttonBackground = p5Background
   refreshColors()
   # change osc base message
   base = "/player5/"
def setPlayer6(pushed):
   global buttonForeground, p6Foreground, buttonBackground, p6Background, base
   # change gui color scheme based on the player selected
   buttonForeground = p6Foreground
   buttonBackground = p6Background
   refreshColors()
   # change osc base message
   base = "/player6/"

def moveUp(pushed):
   global direction
   if pushed:
      # set the direction of the snake
      direction = "UP"
      # tell the snake to move
      oscOut.sendMessage(str(base + direction))
def moveDown(pushed):
   global direction
   if pushed:
      # set the direction of the snake
      direction = "DOWN"
      # tell the snake to move
      oscOut.sendMessage(str(base + direction))
def moveLeft(pushed):
   global direction
   if pushed:
      # set the direction of the snake
      direction = "LEFT"
      # tell the snake to move
      oscOut.sendMessage(str(base + direction))
def moveRight(pushed):
   global direction
   if pushed:
      # set the direction of the snake
      direction = "RIGHT"
      # tell the snake to move
      oscOut.sendMessage(str(base + direction))

"""
Gui Starts Here
"""
# selector color scheme
p1Foreground = Color(124, 10, 2)
p1Background = Color(210, 18, 46)
p2Foreground = Color(8, 37, 103)
p2Background = Color(75, 156, 211)
p3Foreground = Color(28, 53, 45)
p3Background = Color(63, 112, 77)
p4Foreground = Color(245, 199, 26)
p4Background = Color(255, 247, 0)
p5Foreground = Color(195, 82, 20)
p5Background = Color(245, 118, 26)
p6Foreground = Color(114, 36, 108)
p6Background = Color(224, 176, 255)

# default color scheme (when player 1 is selected)
buttonForeground = p1Foreground
buttonBackground = p1Background

# default base OSC message
base = "/player1/"

# draw the screen
d = Display("Control Panel", 800, 600, 0, 0, Color.WHITE)

# load icons
header       = Icon("header.png")
upArrow      = Icon("upArrow.png")
downArrow    = Icon("downArrow.png")
leftArrow    = Icon("leftArrow.png")
rightArrow   = Icon("rightArrow.png")
snakeSelect1 = Icon("snakeSelect.png")
snakeSelect2 = Icon("snakeSelect.png")
snakeSelect3 = Icon("snakeSelect.png")
snakeSelect4 = Icon("snakeSelect.png")
snakeSelect5 = Icon("snakeSelect.png")
snakeSelect6 = Icon("snakeSelect.png")

# buttons to select each player
p1 = Push(25,  25, 100,  75, setPlayer1, p1Foreground, p1Background, Color.WHITE, 0)
p2 = Push(25, 125, 100, 175, setPlayer2, p2Foreground, p2Background, Color.WHITE, 0)
p3 = Push(25, 225, 100, 275, setPlayer3, p3Foreground, p3Background, Color.WHITE, 0)
p4 = Push(25, 325, 100, 375, setPlayer4, p4Foreground, p4Background, Color.WHITE, 0)
p5 = Push(25, 425, 100, 475, setPlayer5, p5Foreground, p5Background, Color.WHITE, 0)
p6 = Push(25, 525, 100, 575, setPlayer6, p6Foreground, p6Background, Color.WHITE, 0)

# directional buttons
up    = Push(350, 150, 550, 250, moveUp, buttonForeground, buttonBackground, Color.WHITE, 0)
down  = Push(350, 450, 550, 550, moveDown, buttonForeground, buttonBackground, Color.WHITE, 0)
left  = Push(200, 300, 400, 400, moveLeft, buttonForeground, buttonBackground, Color.WHITE, 0)
right = Push(500, 300, 700, 400, moveRight, buttonForeground, buttonBackground, Color.WHITE, 0)

# add buttons to gui
d.add(p1)
d.add(p2)
d.add(p3)
d.add(p4)
d.add(p5)
d.add(p6)

d.add(up)
d.add(down)
d.add(left)
d.add(right)

# add icons to gui
d.add(header, 150, 0)

d.add(upArrow, 350, 150)
d.add(downArrow, 350, 450)
d.add(rightArrow, 500, 300)
d.add(leftArrow, 200, 300)

d.add(snakeSelect1, 25, 25)
d.add(snakeSelect2, 25, 125)
d.add(snakeSelect3, 25, 225)
d.add(snakeSelect4, 25, 325)
d.add(snakeSelect5, 25, 425)
d.add(snakeSelect6, 25, 525)

# create OSC to send messages
oscOut = OscOut(IPaddress, 57110)
