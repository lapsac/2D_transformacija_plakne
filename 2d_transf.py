# Programmējamais kods
import numpy as np
import matplotlib.pyplot as plt
import math
img=np.ones((1000,1000,3)) #trīs krāsu kanāli

point1=(300,100)
point2=(100,100)
point3=(100,300)
point4=(300,300)

def MoveObject(move_x, move_y):
    x1=point1[0]+move_x#piekļūšana point 1
    y1=point1[1]+move_y
    
    x2=point2[0]+move_x#piekļūšana point 2
    y2=point2[1]+move_y
    
    x3=point3[0]+move_x#piekļūšana point 3
    y3=point3[1]+move_y
    
    x4=point4[0]+move_x#piekļūšana point 4
    y4=point4[1]+move_y
    
    x5=[x1,x2,x3,x4,x1]#savieno visas x virsotnes
    y5=[y1,y2,y3,y4,y1]#savieno visas y virsotnes
    plt.plot(x5,y5)
    
def ScaleObject(scale_x, scale_y):
    x1=point1[0]*scale_x #piekļūšana point 1
    y1=point1[1]*scale_y
    
    x2=point2[0]*scale_x #piekļūšana point 2
    y2=point2[1]*scale_y
    
    x3=point3[0]*scale_x #piekļūšana point 3
    y3=point3[1]*scale_y
    
    x4=point4[0]*scale_x
    y4=point4[1]*scale_y
    
    # objekta savienošana
    x5=[x1,x2,x3,x4,x1]#savieno visas x virsotnes
    y5=[y1,y2,y3,y4,y1]#savieno visas y virsotnes
    plt.plot(x5,y5)#zīmē līnijas starp virsotnēm

def RotateObject(rotate):
    math.radians(rotate)
    x1=point1[0]*math.cos(rotate)-point1[1]*math.sin(rotate)
    y1=point1[0]*math.sin(rotate)+point1[1]*math.cos(rotate)
    
    x2=point2[0]*math.cos(rotate)-point2[1]*math.sin(rotate)
    y2=point2[0]*math.sin(rotate)+point2[1]*math.cos(rotate)
    
    x3=point3[0]*math.cos(rotate)-point3[1]*math.sin(rotate)
    y3=point3[0]*math.sin(rotate)+point3[1]*math.cos(rotate)
    
    x4=point4[0]*math.cos(rotate)-point4[1]*math.sin(rotate)
    y4=point4[0]*math.sin(rotate)+point4[1]*math.cos(rotate)
    
    # objekta savienošana
    x5=[x1,x2,x3,x4,x1]
    y5=[y1,y2,y3,y4,y1]
    plt.plot(x5,y5)
    
plt.figure(figsize=(5,5),dpi=100, facecolor='w')
plt.imshow(img)
MoveObject (200,200)
ScaleObject(3,3)
RotateObject(90)

plt.show()
