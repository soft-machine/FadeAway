from __future__ import division
from time import sleep
import time

#Import the PCA9685 module.
import Adafruit_PCA9685

#Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 200  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

########### variables for laser written characters ###########

letterHeight = 20 #for best results, should be divisible by four
letterWidth = 10  #for best results, should be divisible by four

xLowBoundary = 1295
yLowBoundary = 1410

xHighBoundary = 1810
yHighBoundary = 1830

xPos = xLowBoundary
yPos = yLowBoundary

#laserPin = 7
xServoPin = 0
yServoPin = 1

inString = "Hello World"

#pinMode(laserPin, OUTPUT)

"""
#Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
"""

#Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def drawA():
  moveOff(0, letterHeight)
  moveOn(letterWidth/2, letterHeight*-1)
  moveOn(letterWidth/2, letterHeight)
  moveOff(0, letterHeight/-2)
  moveOn(letterWidth*-1, 0)
  moveOff(letterWidth, letterHeight/-2)

def drawB():
  moveOn(0, letterHeight)
  moveOn(letterWidth, letterHeight/-4)
  moveOn(letterWidth*-1, letterHeight/-4)
  moveOn(letterWidth, letterHeight/-4)
  moveOn(letterWidth*-1, letterHeight/-4)
  moveOff(letterWidth, 0)

def drawC():
  moveOff(letterWidth, letterHeight/4)
  moveOn(letterWidth/-2, letterHeight/-4)
  moveOn(letterWidth/-2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/-4)
  moveOff(0, (letterHeight/-4)*3)

def drawD():
  moveOn(0, letterHeight)
  moveOn(letterWidth/2, 0)
  moveOn(letterWidth/2, letterHeight/-2)
  moveOn(letterWidth/-2, letterHeight/-2)
  moveOn(letterWidth/-2, 0)
  moveOff(letterWidth, 0)

def drawE():
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight/2)
  moveOn(letterWidth*-1, 0)
  moveOff(0, letterHeight/2)
  moveOn(letterWidth, 0)
  moveOff(letterWidth*-1, 0)
  moveOn(0, letterHeight*-1)
  moveOff(letterWidth, 0)

def drawF():
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight/2)
  moveOn(letterWidth*-1, 0)
  moveOff(0, letterHeight/-2)
  moveOn(0, letterHeight)
  moveOff(letterWidth, letterHeight*-1)

def drawG():
  moveOff(letterWidth, letterHeight/4)
  moveOn(letterWidth/-2, letterHeight/-4)
  moveOn(letterWidth/-2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/-4)
  moveOn(letterWidth/-2, 0)
  moveOff(letterWidth/2, (letterHeight/-4)*3)

def drawH():
  moveOn(0, letterHeight)
  moveOff(0, letterHeight/-2)
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight/2)
  moveOn(0, letterHeight*-1)

def drawI():
  moveOff(letterWidth/2, 0)
  moveOn(0, letterHeight)
  moveOff(letterWidth/2, letterHeight*-1)

def drawJ():
  moveOff(letterWidth, 0)
  moveOn(0, letterHeight)
  moveOn(letterWidth*-1, 0)
  moveOn(0, letterHeight/-4)
  moveOff(letterWidth, (letterHeight/-4)*3)

def drawK():
  moveOn(0, letterHeight)
  moveOff(0, letterHeight/-2)
  moveOn(letterWidth, letterHeight/2)
  moveOff(letterWidth*-1, letterHeight/-2)
  moveOn(letterWidth, letterHeight/-2)

def drawL():
  moveOn(0, letterHeight)
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight*-1)

def drawM():
  moveOff(0, letterHeight)
  moveOn(0, letterHeight * -1)
  moveOn(letterWidth/2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/-2)
  moveOn(0,letterHeight)
  moveOff(0, letterHeight * -1)

def drawN():
  moveOff(0, letterHeight)
  moveOn(0, letterHeight*-1)
  moveOn(letterWidth, letterHeight)
  moveOn(0, letterHeight*-1)

def drawO():
  moveOn(0, letterHeight)
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight*-1)
  moveOn(letterWidth*-1, 0)
  moveOff(letterWidth, 0)

def drawP():
  moveOff(0, letterHeight)
  moveOn(0, letterHeight*-1)
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight/2)
  moveOn(letterWidth*-1, 0)
  moveOff(letterWidth, letterHeight/-2)

def drawQ():
  moveOn(0, letterHeight)
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight*-1)
  moveOn(letterWidth*-1, 0)
  moveOff(letterWidth/2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/2)
  moveOff(0,letterHeight*-1)

def drawR():
  moveOff(0, letterHeight)
  moveOn(0, letterHeight*-1)
  moveOn(letterWidth, letterHeight/4)
  moveOn(letterWidth*-1, letterHeight/4)
  moveOn(letterWidth, letterHeight/2)
  moveOff(0,letterHeight*-1)

def drawS():
  moveOff(letterWidth, 0)
  moveOn(letterWidth*-1, 0)
  moveOn(0, letterHeight/2)
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight/2)
  moveOn(letterWidth*-1,0)
  moveOff(letterWidth, letterHeight* -1)

def drawT():
  moveOn(letterWidth, 0)
  moveOff((letterWidth/-2), 0)
  moveOn(0, letterHeight)
  moveOff(letterWidth/2, letterHeight*-1)

def drawU():
  moveOn(0, letterHeight)
  moveOn(letterWidth, 0)
  moveOn(0,letterHeight*-1)

def drawV():
  moveOn(letterWidth/2, letterHeight)
  moveOn(letterWidth/2, letterHeight*-1)

def drawW():
  moveOn(letterWidth/4, letterHeight)
  moveOn(letterWidth/4, letterHeight/-2)
  moveOn(letterWidth/4, letterHeight/2)
  moveOn(letterWidth/4, letterHeight*-1)

def drawX():
  moveOn(letterWidth, letterHeight)
  moveOff(letterWidth*-1, 0)
  moveOn(letterWidth, letterHeight*-1)

def drawY():
  moveOn(letterWidth/2, letterHeight/2)
  moveOn(0, letterHeight/2)
  moveOff(0, letterHeight/-2)
  moveOn(letterWidth/2, letterHeight/-2)

def drawZ():
  moveOn(letterWidth, 0)
  moveOn(letterWidth*-1, letterHeight)
  moveOn(letterWidth, 0)
  moveOff(0,letterHeight*-1)

def drawSpace():
  moveOff(letterWidth, 0)

def drawPeriod():
  moveOff(0,letterHeight)
  moveOn(0,0)
  moveOff(0,letterHeight*-1)

def drawComma():
  moveOff(0,(letterHeight/4)*3)
  moveOn(letterWidth/-4,letterHeight/4)
  moveOff(letterWidth/4,letterHeight*-1)

def drawColon():
  moveOff(0,letterHeight/4)
  moveOn(0,0)
  moveOff(0, letterHeight/2)
  moveOn(0,0)
  moveOff(0, (letterHeight/4)*-3)

def drawSemicolon():
  moveOff(0,letterHeight/4)
  moveOn(0,0)
  moveOff(0, letterHeight/2)
  moveOn(0,letterHeight/4)
  moveOff(0, letterHeight*-1)

def drawApostrophe():
  moveOn(0,letterHeight/4)
  moveOff(0,letterHeight/-4)

def drawExclamationPoint():
  moveOn(0, (letterHeight/4)*3)
  moveOff(0, letterHeight/4)
  moveOn(0,0)
  moveOff(0,letterHeight*-1)

def drawDash():
 moveOff(0, letterHeight/2)
 moveOn(letterWidth, 0)
 moveOff(0, letterHeight/-2)

def drawForwardSlash():
  moveOff(0, letterHeight)
  moveOn(letterWidth, letterHeight*-1)

def drawBackSlash():
  moveOn(letterWidth, letterHeight)
  moveOff(0,letterHeight*-1)

def drawOpenParens():
  moveOff(letterWidth/2, 0)
  moveOn(letterWidth/-2, letterHeight/2)
  moveOn(letterWidth/2, letterHeight/2)
  moveOff(letterWidth/2, letterHeight *-1)

def drawClosedParens():
  moveOff(letterWidth/2, 0)
  moveOn(letterWidth/2, letterHeight/2)
  moveOn(letterWidth/-2, letterHeight/2)
  moveOff(letterWidth/2, letterHeight * -1)

def drawHash():
  moveOff(letterWidth/4, 0)
  moveOn(0,letterHeight)
  moveOff(letterWidth/2, 0)
  moveOn(0,letterHeight *-1)
  moveOff(letterWidth/4, letterHeight/4)
  moveOn(letterWidth*-1, 0)
  moveOff(0, letterHeight/2)
  moveOn(letterWidth, 0)
  moveOff(0, (letterHeight/-4)*3)

def drawAtSign():
  moveOff(0, letterHeight)
  moveOn(0,letterHeight*-1)
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight)
  moveOn(letterWidth/-4, letterHeight/-4)
  moveOn(0, letterHeight/-4)
  moveOn(letterWidth/-4, 0)
  moveOn(0, letterHeight/4)
  moveOn(letterWidth/4, 0)
  moveOff((letterWidth/4)*3, (letterHeight/4)*-3)

def drawOne():
  moveOff(letterWidth/4, 0)
  moveOn(letterWidth/4, 0)
  moveOn(0, letterHeight)
  moveOff(letterWidth/2, letterHeight*-1)

def drawTwo():
  moveOn(letterWidth, 0)
  moveOn(0, letterHeight/2)
  moveOn(letterWidth*-1, 0)
  moveOn(0, letterHeight/2)
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight*-1)

def drawThree():
  moveOn(letterWidth,0)
  moveOn(0, letterHeight)
  moveOn(letterWidth*-1, 0)
  moveOff(0, letterHeight/-2)
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight/-2)

def drawFour():
  moveOn(0, letterHeight/2)
  moveOn(letterWidth, 0)
  moveOff(0, letterHeight/-2)
  moveOn(0, letterHeight)
  moveOff(0, letterHeight*-1)

def drawSix():
    moveOff(0,letterHeight/2)
    moveOn(letterWidth,0)
    moveOn(0,letterHeight/2)
    moveOn(letterWidth*-1, 0)
    moveOn(0, letterHeight*-1)
    moveOn(letterWidth, 0)

def drawSeven():
    moveOn(letterWidth, 0)
    moveOn(letterWidth/-2, letterHeight)
    moveOff(letterWidth/2, letterHeight*-1)

def drawEight():
    moveOn(0, letterHeight)
    moveOn(letterWidth, 0)
    moveOn(0, letterHeight*-1)
    moveOn(letterWidth*-1, 0)
    moveOff(0, letterHeight/2)
    moveOn(letterWidth, 0)
    moveOff(0, letterHeight/-2)

def drawNine():
    moveOff(letterWidth, letterHeight/2)
    moveOn(letterWidth*-1, 0)
    moveOn(0,letterHeight/-2)
    moveOn(letterWidth, 0)
    moveOn(0, letterHeight)
    moveOn(letterWidth*-1, 0)
    moveOff(letterWidth, letterHeight *-1)

def moveOn(xGo, yGo):
    global xPos
    global yPos
    #digitalWrite(laserPin, HIGH)
    xPos = xPos + xGo
    yPos = yPos + yGo
    pwm.set_pwm(xServoPin, 0, xPos)
    pwm.set_pwm(yServoPin, 0, yPos)
    sleep(.075)
    #digitalWrite(laserPin, LOW)

def moveOff (xGo, yGo):
    global xPos
    global yPos
    xPos = xPos + xGo
    yPos = yPos + yGo
    pwm.set_pwm(xServoPin, 0, xPos)
    pwm.set_pwm(yServoPin, 0, yPos)
    sleep(.075)

def updatePosition():
  pwm.set_pwm(xServoPin, 0, xPos)
  pwm.set_pwm(yServoPin, 0, yPos)
  delay(75)

charcase = {"a": drawA(),
            "A": drawA(),
            "b": drawB(),
            "B": drawB(),
            "c": drawC(),
            "C": drawC(),
            "d": drawD(),
            "D": drawD(),
            "e": drawE(),
            "E": drawE(),
            "f": drawF(),
            "F": drawF(),
            "g": drawG(),
            "G": drawG(),
            "h": drawH(),
            "H": drawH(),
            "i": drawI(),
            "I": drawI(),
            "j": drawJ(),
            "J": drawJ(),
            "k": drawK(),
            "K": drawK(),
            "l": drawK(),
            "L": drawL(),
            "m": drawM(),
            "M": drawM(),
            "n": drawN(),
            "N": drawN(),
            "o": drawO(),
            "O": drawO(),
            "p": drawP(),
            "P": drawP(),
            "q": drawQ(),
            "Q": drawQ(),
            "r": drawR(),
            "R": drawR(),
            "s": drawS(),
            "S": drawS(),
            "t": drawT(),
            "T": drawT(),
            "u": drawU(),
            "U": drawU(),
            "v": drawV(),
            "V": drawV(),
            "w": drawW(),
            "W": drawW(),
            "x": drawX(),
            "X": drawX(),
            "y": drawY(),
            "Y": drawY(),
            "z": drawZ(),
            "Z": drawZ(),
            " ": drawSpace(),
            ".": drawPeriod(),
            ",": drawComma(),
            ":": drawColon(),
            "": drawSemicolon(),
            "!": drawExclamationPoint(),
            "\"": drawApostrophe(),#apostrophe/quotation-mark
            "-": drawDash(),
            "\\": drawBackSlash(),
            "/": drawForwardSlash(),
            #"(":
            "<": drawOpenParens(),
            #")":
            ">": drawClosedParens(),
            "#": drawHash(),
            "@": drawAtSign(),
            "1": drawOne(),
            "2": drawTwo(),
            "3": drawThree(),
            "4": drawFour(),
            "5": drawS(),# ISWYDT
            "6": drawSix(),
            "7": drawSeven(),
            "8": drawEight(),
            "9": drawNine(),
            "0": drawO()
}

while True:

    print "type whatever you like"
    inString = raw_input()
    print "you typed = ",inString

    for i in range(len(inString)):
        c = inString[i]

        #servo write corresponding char
        charcase[c]()

        #character line wrap
        if xPos + letterWidth > xHighBoundary:
            yPos = yPos + letterHeight + 5
            xPos = xLowBoundary
            updatePosition()
            sleep(0.1)

        #panel wrap
        if yPos + letterHeight > yHighBoundary:
            yPos = yLowBoundary
            xPos = xLowBoundary
            updatePosition()
            sleep(0.1)

    # clear our string
    del inString
    sleep(2)
    # End main loop

