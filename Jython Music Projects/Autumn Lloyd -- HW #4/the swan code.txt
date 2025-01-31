# theSwanImage.py
#
# Author:  Autumn R Lloyd
# Email:   lloydar@g.cofc.edu
# Class:   Computers Music Art FYSE  
# Assignment: Homework #4
# Due Date:  4 November 2022
#
# Purpose: Recreates The Swan, an abstract piece created by Hilma af Klint
#
# Image found at:
# https://uploads7.wikiart.org/00140/images/hilma-af-klint/hilma-af-klint-svanen.jpg

from gui import *

# making my colors consistient
blue       = Color(78,131,183)
yellow     = Color(220,178,80)
lightPink  = Color(225,163,146)
pink       = Color(218,129,108)
black      = Color(30,30,30)
white      = Color(222,214,203)
red        = Color(172,52,36)
darkerRed  = Color(163,62,40)
darkestRed = Color(145,69,51)
red        = Color(150,62,40)

#creating display
theSwan = Display("The Swan", 500, 500, 0, 0, red)

#width and height contstants
WIDTH  = theSwan.getWidth()
HEIGHT = theSwan.getHeight()

#background gradation for my sanity and to get more objects
gradientOne   = Circle((WIDTH/2), (HEIGHT/2), 250, darkestRed, True)
gradientTwo   = Circle((WIDTH/2), (HEIGHT/2), 200, darkerRed, True)
gradientThree = Circle((WIDTH/2), (HEIGHT/2), 150, red, True)
gradientFour  = Circle((WIDTH/2), (HEIGHT/2), 300, darkerRed, True)

# drawing arcs
blueArc       = Arc((WIDTH / 2) - 100 , 150, (WIDTH / 2) + 100, 350, 270, 450, blue, True)
whiteArc      = Arc((WIDTH / 2) - 100 , 150, (WIDTH / 2) + 100, 350, 90, 270, white, True)
blackArc      = Arc((WIDTH / 2) - 75 , 175, (WIDTH / 2) + 75, 325, 90, 270, black, True)
yellowArc     = Arc((WIDTH / 2) - 75 , 175, (WIDTH / 2) + 75, 325, 270, 450, yellow, True)
lightPinkArc  = Arc((WIDTH / 2) - 50 , 200, (WIDTH / 2) + 50, 300, 270, 450, lightPink, True)
pinkArc       = Arc((WIDTH / 2) - 25 , 225, (WIDTH / 2) + 25, 275, 270, 450, pink, True)
smallBlackArc = Arc((WIDTH / 2) - 5 , 245, (WIDTH / 2) + 5, 255, 270, 450, black, True)
smallPinkArc  = Arc((WIDTH / 2) - 5 , 245, (WIDTH / 2) + 5, 255, 90, 270, pink, True)

#adding to display
theSwan.add(gradientFour)
theSwan.add(gradientOne)
theSwan.add(gradientTwo)
theSwan.add(gradientThree)

theSwan.add(blueArc)
theSwan.add(whiteArc)
theSwan.add(blackArc)
theSwan.add(yellowArc)
theSwan.add(lightPinkArc)
theSwan.add(pinkArc)
theSwan.add(smallBlackArc)
theSwan.add(smallPinkArc)