# snakeGameOSCFinal.1.py
#
# Author:  Autumn Rose Lloyd
# Email:   lloydar@g.cofc.edu
# Class:   CITA 284 / CSCI 299
# Assignment: Final Project
# Due Date:  28 April 2023
#
# Purpose: This program generates a game of multiplayer snake.
#
# Input:   Users use a custon Gui to control all six snakes.
#
# Output:  Six snakes move, grow, and compete to become the longest snake or the last one standing.
#
# Sounds from:
#     snakeWall:        https://freesound.org/people/Greenhourglass/sounds/159376/
#     snakeDie:         https://freesound.org/people/Greenhourglass/sounds/159377/
#     appleCollide:     https://freesound.org/people/Greenhourglass/sounds/159379/
#     background music: https://freesound.org/people/SintelV/sounds/669551/
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
from music import *
from random import *

"""
Create game elements based on an object oriented approach.
"""

# constants = key codes
UP    = 38
DOWN  = 40
LEFT  = 37
RIGHT = 39

# snake parts
HEAD = "HEAD"
BODY = "BODY"

class Segment(Rectangle):
   """
   creates a segment based off of a center point, width, and direction
   """
   global UP, DOWN, LEFT, RIGHT, HEAD, BODY
   def __init__(self, xCenter, yCenter, radius, direction, iconSet, bodyPart = BODY):
      
      # establish segment identity
      self.xCenter      = xCenter
      self.yCenter      = yCenter
      self.radius       = radius
      self.direction    = direction 
      self.iconSet      = iconSet
      self.headStates   = self.iconSet[0]
      self.bodyPart     = bodyPart
      
      # shift given points over
      self.x1 = int(self.xCenter - (self.radius/2))
      self.y1 = int(self.yCenter - (self.radius/2))
      self.x2 = int(self.xCenter + (self.radius/2))
      self.y2 = int(self.yCenter + (self.radius/2))
      
      # what body part?
      if self.bodyPart == HEAD:
         if self.direction == UP:
            self.icon = self.headStates[0]
         elif self.direction == DOWN:
            self.icon = self.headStates[1]
         elif self.direction == LEFT:
            self.icon = self.headStates[2]
         elif self.direction == RIGHT:
            self.icon = self.headStates[3]  
      elif self.bodyPart == BODY:
         self.icon = self.iconSet[1]
         
      Rectangle.__init__(self, self.x1, self.y1, self.x2, self.y2, Color.BLACK, False, 0)
      
         
   def __str__(self):
      message = "Segment with width of " + str(self.radius) + " pixels at position (" + str(self.xCenter) + ", " + str(self.yCenter) + ") facing " + str(self.direction)
      return message
   
   # check center points?
   def getX(self):
      return self.xCenter
   
   def getY(self):
      return self.yCenter
   
   def setX(self, x):
      self.xCenter = x
      
   def setY(self, y):
      self.yCenter = y
   
   # check direction?
   def getDirection(self):
      return self.direction
   
   def setDirection(self, direction):
      self.direction = direction
   
   # get size   
   def getRadius(self):
      return self.radius
   
   # get icon x and y
   def getX1(self):
      return self.x1
   def getY1(self):
      return self.y1
   
   # what icon?
   def getIcon(self):
      # check what body part / direction
      if self.bodyPart == HEAD:
         if self.direction == UP:
            self.icon = self.headStates[0]
         elif self.direction == DOWN:
            self.icon = self.headStates[1]
         elif self.direction == LEFT:
            self.icon = self.headStates[2]
         elif self.direction == RIGHT:
            self.icon = self.headStates[3]  
      elif self.bodyPart == BODY:
         self.icon = self.iconSet[1]
      # fetch correct icon    
      return self.icon
      
class Snake:
   """
   creates a snake based on the Segment class
   
   The head of the snake will always be at self.segments[0]
   """
   global UP, DOWN, LEFT, RIGHT, HEAD, BODY
   def __init__(self, x, y, direction, display, iconSet):
      # establish snake identity 
      self.x         = x
      self.y         = y
      self.segments  = []
      self.icons     = []
      self.display   = display
      self.radius    = int(self.display.getHeight() * .05)
      self.alive     = True
      self.direction = direction
      self.iconSet   = iconSet
      
      # create the head
      head = Segment(self.x, self.y, self.radius, self.direction, self.iconSet, HEAD)
      self.segments.append(head)
      self.display.add(head)
      self.icons.append(Icon(head.getIcon(), self.radius, self.radius))
      self.display.add(self.icons[0], head.getX(), head.getY())
      
   def __str__(self):
      message = "Snake with segments: \n" 
      for segment in self.segments:
         message += str(segment) + "\n"
      return message
      
   def __addSegment(self):
      # where is previous segment?
      prevX = self.segments[len(self.segments) - 1].getX()
      prevY = self.segments[len(self.segments) - 1].getY()
      prevDirection = self.segments[len(self.segments) - 1].getDirection()
      
      # add new segment behind previous segment
      if prevDirection == UP:
         offsetX = int(prevX)
         offsetY = int(prevY + self.radius)
      elif prevDirection == DOWN:
         offsetX = int(prevX)
         offsetY = int(prevY - self.radius)
      elif prevDirection == LEFT:
         offsetX = int(prevX + self.radius)
         offsetY = int(prevY)
      elif prevDirection == RIGHT:
         offsetX = int(prevX - self.radius)
         offsetY = int(prevY)
      
      # draw new segment to screen
      newSegment = Segment(offsetX, offsetY, self.radius, prevDirection, self.iconSet)
      self.segments.append(newSegment)
      self.display.add(newSegment)
      self.icons.append(Icon(newSegment.getIcon(), self.radius, self.radius))
      self.display.add(self.icons[len(self.segments) - 1], newSegment.getX(), newSegment.getY())
   
   # if snake eats apple, grow   
   def __eat(self, apple):
      Snake.__addSegment(self)
      apple.eaten()
      snakeAppleSound.play()
   
   # if snake breaks rule, die      
   def __die(self):
      if self.alive == True:
         snakeSnakeSound.play()
      self.alive = False
      # remove icons
      for icon in self.icons:
         self.display.remove(icon)
      for segment in self.segments:
         # remove segment visually
         self.display.remove(segment)
         # prevent living snake from colliding with dead snake
         segment.setX(-9999)
         segment.setY(-9999)
   
   # if snake hits the wall, move backwards
   def __stuck(self):
      if self.alive == True:
         snakeWallSound.play()
         # check direction of head to place snake back on screen
         if self.segments[0].getDirection() == UP:
            for segment in self.segments:
               segment.setY(segment.getY() + self.radius * 2)
               self.display.add(segment)
         elif self.segments[0].getDirection() == DOWN:
            for segment in self.segments:
               segment.setY(segment.getY() - self.radius * 2)
               self.display.add(segment)
         elif self.segments[0].getDirection() == LEFT:
            for segment in self.segments:
               segment.setX(segment.getX() + self.radius * 2)
               self.display.add(segment)
         elif self.segments[0].getDirection() == RIGHT:
            for segment in self.segments:
               segment.setX(segment.getX() - self.radius * 2)
               self.display.add(segment)
         # update icons
         for index in range(len(self.icons)):
            self.display.remove(self.icons[index])
            self.icons[index] = Icon(self.segments[index].getIcon(), self.radius, self.radius)
            self.display.add(self.icons[index], self.segments[index].getX(), self.segments[index].getY())
      
   
   def moveSnake(self, direction): 
      # is move legal?
      if     self.alive == False:   # if snake is dead, don't move 
         pass
      elif   self.segments[0].getDirection() == UP    and direction == DOWN:
         pass
      elif self.segments[0].getDirection() == DOWN  and direction == UP:
         pass
      elif self.segments[0].getDirection() == LEFT  and direction == RIGHT:
         pass
      elif self.segments[0].getDirection() == RIGHT and direction == LEFT:
         pass
      else:
         for index in range(len(self.segments) - 1, 0, -1):
            # have segment follow previous segment (take its direction)
            if index > 0:
               self.segments[index].setDirection(self.segments[index - 1].getDirection())
         # set direction of head based on user input
         self.segments[0].setDirection(direction)
            
         # move snake based on direction of each segment
         for segment in self.segments:
            if segment.getDirection() == UP:
               offsetX = 0
               offsetY = int(- self.radius)
            elif segment.getDirection() == DOWN:
               offsetX = 0
               offsetY = int(self.radius)
            elif segment.getDirection() == LEFT:
               offsetX = int(- self.radius)
               offsetY = 0
            elif segment.getDirection() == RIGHT:
               offsetX = int(self.radius)
               offsetY = 0
            # draw each segment!
            segment.setX(offsetX + segment.getX())
            segment.setY(offsetY + segment.getY())
            self.display.add(segment)
         # update icons
         for index in range(len(self.icons)):
            self.display.remove(self.icons[index])
            self.icons[index] = Icon(self.segments[index].getIcon(), self.radius, self.radius)
            self.display.add(self.icons[index], self.segments[index].getX(), self.segments[index].getY())
 
   def checkSnakeCollide(self, snake):
      # if any part of either snake overlaps, die
      for segment in self.segments:
         for otherSegment in snake.getSegments():
            if ( segment.getX() <= otherSegment.getX() + otherSegment.getRadius()* 2 and segment.getX() >= otherSegment.getX() - otherSegment.getRadius()* 2 and 
                 segment.getY() <= otherSegment.getY() + otherSegment.getRadius()* 2 and segment.getY() >= otherSegment.getY() - otherSegment.getRadius()* 2     ):
               Snake.__die(self)
               
      # if snake touches itself, die
      for i in range(1, len(self.segments)):
         if self.segments[0].getX() == self.segments[i].getX() and self.segments[0].getY() == self.segments[i].getY():
            Snake.__die(self)
      
      # if snake runs into wall, stop the snake
      if self.segments[0].getX() < self.radius * 2 or self.segments[0].getY() < self.radius * 2 or self.segments[0].getX() > self.display.getWidth() - self.radius * 2 or self.segments[0].getY() > self.display.getHeight() - self.radius * 2:
         Snake.__stuck(self)
         
   def checkAppleCollide(self, apple):
      # if head of snake touches apple, eat apple
      if  (apple.getX() >= self.segments[0].getX() - (self.radius + apple.getRadius()/2) and apple.getX() <= self.segments[0].getX() + self.radius + apple.getRadius()/2 and 
           apple.getY() >= self.segments[0].getY() - (self.radius + apple.getRadius()/2) and apple.getY() <= self.segments[0].getY() + self.radius + apple.getRadius()/2   ):
         Snake.__eat(self, apple)
   
   # how long is snake?      
   def getSegments(self):
      return self.segments
   
   # how wide is each segment?
   def getRadius(self):
      return self.radius
   
   # is snake alive?
   def getAlive(self):
      return self.alive
      

class Apple():
   """
   creates apples for snakes to eat and then grow
   each apple is randomly placed anywhere on the screen
   """
   def __init__(self, xGrid, yGrid, display):
      # establish apple identity
      self.display = display
      self.radius  = int(self.display.getHeight() * .05)
      self.xGrid   = xGrid
      self.yGrid   = yGrid
      self.xPos    = choice(self.xGrid) - (self.radius/2)
      self.yPos    = choice(self.yGrid) - (self.radius/2)
      self.apple   = Icon("appleIcon.png", self.radius, self.radius)
      
      # draw apple on screen
      self.display.add(self.apple, self.xPos, self.yPos)
   
   def __str__(self):
      message = "Apple at (" + str(self.xPos) + ", " + str(self.yPos) + ") with radius of " + str(self.radius)
      return message
   
   # if snake eats apple, remove apple and make new one
   def eaten(self):
      self.display.remove(self.apple)
      Apple.__init__(self, self.xGrid, self.yGrid, self.display)
   
   # what is x, y, radius?
   def getX(self):
      return self.xPos
   
   def getY(self):
      return self.yPos
   
   def getRadius(self):
      return self.radius

"""
makes the IP Address Accessible 
"""
class AccessibleIP(OscIn):
   def __init__(self, port):
      OscIn.__init__(self, port)
   
   def getIP(self):
      return self.IPaddress

"""
replaces my game engine  
"""
def updateSnake(message):
   
   global snake1, snake2, snake3, snake4, snake5, snake6, apple, UP, DOWN, LEFT, RIGHT, endIcon

   # what button is pressed?
   address = message.getAddress()
   # is is user player 1?
   if address[:9] == "/player1/":
      # what direction?
      if address == "/player1/UP":
         direction = UP
      elif address == "/player1/DOWN":
         direction = DOWN
      elif address == "/player1/LEFT":
         direction = LEFT
      elif address == "/player1/RIGHT":
         direction = RIGHT
      # update snake
      snake1.checkSnakeCollide(snake2)
      snake1.checkSnakeCollide(snake3)
      snake1.checkSnakeCollide(snake4)
      snake1.checkSnakeCollide(snake5)
      snake1.checkSnakeCollide(snake6)
      snake1.moveSnake(direction)
      snake1.checkAppleCollide(apple)
      
   # is user player 2?
   elif address[:9] == "/player2/":
      # what direction?
      if address == "/player2/UP":
         direction = UP
      elif address == "/player2/DOWN":
         direction = DOWN
      elif address == "/player2/LEFT":
         direction = LEFT
      elif address == "/player2/RIGHT":
         direction = RIGHT
      # update snake
      snake2.checkSnakeCollide(snake1)
      snake2.checkSnakeCollide(snake3)
      snake2.checkSnakeCollide(snake4)
      snake2.checkSnakeCollide(snake5)
      snake2.checkSnakeCollide(snake6)
      snake2.moveSnake(direction)
      snake2.checkAppleCollide(apple)
      
   # is user player 3?   
   elif address[:9] == "/player3/":
      # what direction?
      if address == "/player3/UP":
         direction = UP
      elif address == "/player3/DOWN":
         direction = DOWN
      elif address == "/player3/LEFT":
         direction = LEFT
      elif address == "/player3/RIGHT":
         direction = RIGHT
      # update snake
      snake3.checkSnakeCollide(snake2)
      snake3.checkSnakeCollide(snake1)
      snake3.checkSnakeCollide(snake4)
      snake3.checkSnakeCollide(snake5)
      snake3.checkSnakeCollide(snake6)
      snake3.moveSnake(direction)
      snake3.checkAppleCollide(apple)
      
   # is user player 4?
   elif address[:9] == "/player4/":
      # what direction?
      if address == "/player4/UP":
         direction = UP
      elif address == "/player4/DOWN":
         direction = DOWN
      elif address == "/player4/LEFT":
         direction = LEFT
      elif address == "/player4/RIGHT":
         direction = RIGHT
      # update snake
      snake4.checkSnakeCollide(snake2)
      snake4.checkSnakeCollide(snake3)
      snake4.checkSnakeCollide(snake1)
      snake4.checkSnakeCollide(snake5)
      snake4.checkSnakeCollide(snake6)
      snake4.moveSnake(direction)
      snake4.checkAppleCollide(apple)
      
   # is user player 5?
   elif address[:9] == "/player5/":
      # what direction?
      if address == "/player5/UP":
         direction = UP
      elif address == "/player5/DOWN":
         direction = DOWN
      elif address == "/player5/LEFT":
         direction = LEFT
      elif address == "/player5/RIGHT":
         direction = RIGHT
      # update snake
      snake5.checkSnakeCollide(snake2)
      snake5.checkSnakeCollide(snake3)
      snake5.checkSnakeCollide(snake4)
      snake5.checkSnakeCollide(snake1)
      snake5.checkSnakeCollide(snake6)
      snake5.moveSnake(direction)
      snake5.checkAppleCollide(apple)
   
   # is user player 6?
   elif address[:9] == "/player6/":
      # what direction?
      if address == "/player6/UP":
         direction = UP
      elif address == "/player6/DOWN":
         direction = DOWN
      elif address == "/player6/LEFT":
         direction = LEFT
      elif address == "/player6/RIGHT":
         direction = RIGHT
      # update snake
      snake6.checkSnakeCollide(snake2)
      snake6.checkSnakeCollide(snake3)
      snake6.checkSnakeCollide(snake4)
      snake6.checkSnakeCollide(snake5)
      snake6.checkSnakeCollide(snake1)
      snake6.moveSnake(direction)
      snake6.checkAppleCollide(apple)
      
   # how many snakes left?
   count = 0
   for snake in [snake1, snake2, snake3, snake4, snake5, snake6]:
      if snake.getAlive():
         count = count + 1
   # if one snake left, you win!
   if count == 1:
      d.add(endIcon, 0, 0)
      bgMusic.stop()
      snakeAppleSound.play()
   
"""
create a grid for objects to appear on
"""
def createGrid(display):
   xGrid = []
   yGrid = []
   
   increment = display.getHeight() * .05 # same width as snake
   valueX = increment
   valueY = increment
   
   # check if point is on screen
   while valueY < display.getHeight() - 2 * increment:
      valueY = valueY + increment
      yGrid.append(int(valueY))
   while valueX < display.getWidth() - 2 * increment:
      valueX = valueX + increment
      xGrid.append(int(valueX))
      
   grid = [xGrid, yGrid]
   return grid 

"""
Game code starts here
"""
# create OSC server for incoming messages
oscIn = AccessibleIP(57110)
oscIn.hideMessages()

# create screen, snakes, and apple
# snakes and apple are assigned random starting places
d = Display("Play the snake game! Join at IP: " + oscIn.getIP(), 1200, 650, 10, 10)
directions = [UP, DOWN, LEFT, RIGHT]
xGrid, yGrid = createGrid(d)

# create background image, add it to the screen
bg = Icon("snakeBackground.png")
d.add(bg, 0, 0)

endIcon = Icon("endIcon.png")

# head icon sets
snake1Head = ["snake1Up.png", "snake1Down.png", "snake1Left.png", "snake1Right.png"]
snake2Head = ["snake2Up.png", "snake2Down.png", "snake2Left.png", "snake2Right.png"]
snake3Head = ["snake3Up.png", "snake3Down.png", "snake3Left.png", "snake3Right.png"]
snake4Head = ["snake4Up.png", "snake4Down.png", "snake4Left.png", "snake4Right.png"]
snake5Head = ["snake5Up.png", "snake5Down.png", "snake5Left.png", "snake5Right.png"]
snake6Head = ["snake6Up.png", "snake6Down.png", "snake6Left.png", "snake6Right.png"]

# snake icon sets
snake1Set = [snake1Head, "snake1Body.png"]
snake2Set = [snake2Head, "snake2Body.png"]
snake3Set = [snake3Head, "snake3Body.png"]
snake4Set = [snake4Head, "snake4Body.png"]
snake5Set = [snake5Head, "snake5Body.png"]
snake6Set = [snake6Head, "snake6Body.png"]

# create snakes, add to screen
snake1 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake1Set)
snake2 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake2Set)
snake3 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake3Set)
snake4 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake4Set)
snake5 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake5Set)
snake6 = Snake(choice(xGrid), choice(yGrid), choice(directions), d, snake6Set)

# create apple, add to screen
apple = Apple(xGrid, yGrid, d)

# load audio
snakeWallSound  = AudioSample("snakeWall.wav")
snakeAppleSound = AudioSample("appleCollide.wav")
snakeSnakeSound = AudioSample("snakeDie.wav")
bgMusic         = AudioSample("bgMusic.wav")

# start game!
bgMusic.loop()
oscIn.onInput("/player.*", updateSnake)
