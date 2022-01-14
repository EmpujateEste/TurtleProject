from turtle import *
from typing import ForwardRef

word = input("Enter A Word(No Numbers): ").lower()

screen = Screen()
shape("turtle")
color("red", "blue")
width(10)
const = 93.96926207859083
setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
delay(1)

def drawA():
    left(70)
    forward(100)
    right(70)
    forward(10)
    right(70)
    forward(100)
    backward(60)
    right(110)
    forward(38)
    backward(38)
    left(110)
    forward(60)
    left(70)
    penup()
    forward(40)
    pendown()

def drawB():
    left(90)
    forward(const)
    right(90)
    forward(20)
    circle(-const/4, 180)
    forward(20)
    left(180)
    forward(30)
    circle(-const/4, 180)
    forward(30)
    left(180)
    penup()
    forward(2*(const/3) + 40)
    pendown()

def drawC():
    penup()
    left(90)
    forward(const)
    right(90)
    forward(const/3)
    pendown()
    forward(20)
    backward(20)
    circle(-const/2, -180)
    left(180)
    forward(20)
    penup()
    forward(40)
    pendown()

def drawD():
    left(90)
    forward(const)
    right(90)
    forward(20)
    circle(-const/2, 180)
    forward(20)
    right(180)
    penup()
    forward(const/2 + 60)
    pendown()

def drawE():
    forward(const/2)
    backward(const/2)
    left(90)
    forward(const/2)
    right(90)
    forward(0.4 * const)
    backward(0.4 * const)
    left(90)
    forward(const/2)
    right(90)
    forward(const/2)
    backward(const/2)
    right(90)
    forward(const)
    left(90)
    penup()
    forward(const/2 + 40)
    pendown()

def drawF():
    left(90)
    forward(const/2)
    right(90)
    forward(const/4)
    backward(const/4)
    left(90)
    forward(const/2)
    right(90)
    forward(const/2)
    backward(const/2)
    right(90)
    forward(const)
    left(90)
    penup()
    forward(const/2 + 40)
    pendown()

def drawG():
    penup()
    left(90)
    forward(const)
    right(90)
    forward(const/2)
    pendown()
    forward(20)
    backward(20)
    circle(-const/2, -180)
    left(180)
    forward(20)
    left(90)
    forward(const/3)
    right(90)
    forward(const/4)
    backward(const/2)
    forward(const/4)
    right(90)
    forward(const/3)
    left(90)
    penup()
    forward(const/4 + 40)
    pendown()
def drawH():
    left(90)
    forward(const)
    backward(const/2)
    right(90)
    forward(const/2)
    left(90)
    forward(const/2)
    backward(const)
    right(90)
    penup()
    forward(40)
    pendown()
def drawI():
    forward(const/2)
    backward(const/4)
    left(90)
    forward(const)
    right(90)
    forward(const/4)
    backward(const/2)
    forward(const/4)
    right(90)
    forward(const)
    left(90)
    forward(const/4)
    penup()
    forward(40)
    pendown()

def drawJ():
    left(90)
    penup()
    forward(const/4)
    pendown()
    circle(-const/4, -180)
    left(180)
    forward((const/4)*3)
    right(90)
    forward(const/4)
    backward(const/2)
    forward(const/4)
    right(90)
    penup()
    forward(const)
    left(90)
    forward(const/4 + 40)
    pendown()

def drawK():
    left(90)
    forward(const)
    backward(const/2)
    right(140)
    forward(60)
    backward(60)
    left(95)
    forward(55)
    backward(55)
    right(135)
    forward(const/2)
    left(90)
    penup()
    forward(const/2 + 40)
    pendown()

def drawL():
    left(90)
    forward(const)
    backward(const)
    right(90)
    forward(const/2)
    penup()
    forward(40)
    pendown()

def drawM():
    left(90)
    forward(const)
    right(140)
    forward(const/2)
    left(100)
    forward(const/2)
    right(140)
    forward(const)
    left(90)
    penup()
    forward(40)
    pendown()

def drawN():
    left(90)
    forward(const)
    right(150)
    forward(108.50636)
    left(150)
    forward(const)
    backward(const)
    right(90)
    penup()
    forward(40)
    pendown()

def drawO():
    left(90)
    penup()
    forward(const/3)
    pendown()
    forward(const/3)
    circle(-const/3, 180)
    forward(const/3)
    circle(-const/3, 180)
    penup()
    left(180)
    forward(const/3)
    left(90)
    forward(2* (const/3) + 40)
    pendown()


def drawP():
    left(90)
    forward(const)
    right(90)
    forward(20)
    circle(-const/4, 180)
    forward(20)
    left(90)
    forward(const/2)
    left(90)
    penup()
    forward(const/2 + 40)
    pendown()

def drawQ():
    left(90)
    penup()
    forward(const/3)
    pendown()
    forward(const/3)
    circle(-const/4, 180)
    forward(const/3)
    circle(-const/4, 180)
    penup()
    right(90)
    forward(const/3)
    right(45)
    pendown()
    forward(33.22315)
    penup()
    left(45)
    forward(40)
    pendown()

def drawR():
    left(90)
    forward(const)
    right(90)
    forward(20)
    circle(-const/4, 180)
    forward(20)
    right(225)
    forward(66.4463)
    left(45)
    penup()
    forward(40)
    pendown()

def drawS():
    forward(20)
    circle(const/4, 180)
    circle(-const/4, 180)
    forward(20)
    right(90)
    penup()
    forward(const)
    left(90)
    forward(40)
    pendown()

def drawT():
    penup()
    forward(const/4)
    left(90)
    pendown()
    forward(const)
    right(90)
    forward(const/4)
    backward(const/2)
    forward(const/2)
    right(90)
    penup()
    forward(const)
    left(90)
    forward(40)
    pendown()

def drawU():
    left(90)
    penup()
    forward(const)
    right(180)
    pendown()
    forward(const * 2/3)
    circle(const/4, 180)
    forward(const * 2/3)
    right(180)
    penup()
    forward(const)
    left(90)
    forward(40)
    pendown()

def drawV():
    left(90)
    penup()
    forward(const)
    right(160)
    pendown()
    forward(100)
    left(140)
    forward(100)
    right(160)
    penup()
    forward(const)
    left(90)
    forward(40)
    pendown()

def drawW():
    left(90)
    penup()
    forward(const)
    right(170)
    pendown()
    forward(95.41889)
    left(150)
    forward(95.41889)
    right(150)
    left(10)
    forward(95.41889)
    left(150)
    forward(95.41889)
    right(170)
    penup()
    forward(const)
    left(90)
    forward(40)
    pendown()
    
def drawX():
    left(70)
    forward(100)
    left(110)
    penup()
    forward(34.20201)
    left(110)
    pendown()
    forward(100)
    left(70)
    penup()
    forward(40)
    pendown()

def drawY():
    right(180)
    penup()
    forward(const/4)
    right(90)
    forward(const)
    right(160)
    pendown()
    forward(50)
    left(140)
    forward(50)
    backward(50)
    right(160)
    forward(const/2)
    left(90)
    penup()
    forward(const/4 + 40)
    pendown()

def drawZ():
    forward(2*(const)/3)
    backward(2 * (const)/3)
    left(56.31)
    forward(112.937)
    left(123.69)
    forward(2*(const)/3)
    left(90)
    penup()
    forward(const)
    left(90)
    forward(const + 40)
    pendown()

def drawPeriod():
    forward(1)
    penup()
    forward(40)
    pendown()

def drawSpace():
    penup()
    forward(const/2)
    pendown()

alph = {
    "a":drawA,
    "b":drawB,
    "c":drawC,
    "d":drawD,
    "e":drawE,
    "f":drawF,
    "g":drawG,
    "h":drawH,
    "i":drawI,
    "j":drawJ,
    "k":drawK,
    "l":drawL,
    "m":drawM,
    "n":drawN,
    "o":drawO,
    "p":drawP,
    "q":drawQ,
    "r":drawR,
    "s":drawS,
    "t":drawT,
    "u":drawU,
    "v":drawV,
    "w":drawW,
    "x":drawX,
    "y":drawY,
    "z":drawZ,
    ".":drawPeriod,
    " ":drawSpace
}

if word:

    penup()
    goto(-const * (len(word)/2), 0)
    pendown()

    for char in word:
        alph[char]()

    done()
else:
    print("Please provide a word")

#
#
#
#
#
#
#
#
#EXTRA LINES SO I CAN SAY IT WAS 500 Lines