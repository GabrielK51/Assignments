# Import the CMU Graphics Package:
from cmu_graphics import *

#head
#Circle(CenterX, CenterY, radius)
Circle(200, 200, 150, fill=gradient('yellow', 'orange'))

#Eyes
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

# Run program:
cmu_graphics.run()
