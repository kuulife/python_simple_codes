import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self): #method
    	return math.sqrt(((self.coor2[0] - self.coor1[0])**2)+((self.coor2[1] - self.coor1[1])**2))
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(f'distance between {coordinate1} and {coordinate2} is: {li.distance()}')
print(f'slope between {coordinate1} and {coordinate2} is: {li.slope()}')