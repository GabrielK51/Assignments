from cmu_graphics import *

Roof = Polygon(300, 140, 220, 30, 135, 140,fill='red')
Home = Rect(135, 140, 165, 145, fill='blue')
Window1 = Rect(235, 170, 50, 50, fill='white')
Window2 = Rect(150, 170, 50, 50, fill='white')
Door = Rect(200, 235, 30, 50, fill='white')

House = Group(Roof,
              Home,
              Window1,
              Window2,
              Door
              )

def onMousePress(MouseX,MouseY):
    House.centerX +=100

def onMouseRelease(MouseX,MouseY):
    House.centerX -=100

cmu_graphics.run()
 
