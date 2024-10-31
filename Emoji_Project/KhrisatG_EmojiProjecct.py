# Import the CMU Graphics Package:
from cmu_graphics import *

#head
#Circle(CenterX, CenterY, radius)
Circle(200, 200, 150, fill=gradient('yellow', 'orange'))

#Eyes
#Label(text, centerX, centerY)
Label('$',150, 150, fill='green', size=100, bold=True)
Label('$',250, 150, fill='green', size=100, bold=True)

#Cheek
#Star(centerX, centerY, radius, points, roundness=none)

Star(325, 200, 20, 5, roundness=20, fill='red')

#Mouth
# Rect(left, top, width, height)
Rect(125, 250, 150, 50)

#Teeth
Rect(125, 250, 37.5, 16.6, fill='white', border='black')
Rect(162.5, 250, 37.5, 16.6, fill='white', border='black')
Rect(200, 250, 37.5, 16.6, fill='white', border='black')
Rect(237.5, 250, 37.5, 16.6, fill='white', border='black')

Rect(125, 283, 37.5, 16.6, fill='white', border='black')
Rect(162.5, 283, 37.5, 16.6, fill='white', border='black')
Rect(200, 283, 37.5, 16.6, fill='white', border='black')
Rect(237.5, 283, 37.5, 16.6, fill='white', border='black')

#Gum

#Oval(centerX, centerY, width, height)

Oval(200, 283, 30, 30, fill=rgb(255, 161, 205))

# Run program:
cmu_graphics.run()
