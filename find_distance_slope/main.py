import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self): #method
    	x1,y1 = self.coor1
    	x2, y2 = self.coor2
    	return math.sqrt((x2 - x1)**2+(y2 - y1)**2)
    
    def slope(self):
    	x1,y1 = self.coor1
    	x2, y2 = self.coor2
    	return (y2 - y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(f'distance between {coordinate1} and {coordinate2} is: {li.distance()}')
print(f'slope between {coordinate1} and {coordinate2} is: {li.slope()}')