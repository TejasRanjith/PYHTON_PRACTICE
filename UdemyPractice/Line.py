class Line():

    def __init__(self, coor1, coor2):
        self.x1, self.y1, self.x2, self.y2 = coor1[0], coor1[1], coor2[0], coor2[1]

    def distance(self):
        return (((self.x2-self.x1)**2) + ((self.y2-self.y1)**2))**(1/2)

    def slope(self):
        return ((self.y2-self.y1)/(self.x2-self.x1))
