from math import sqrt

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    def get_distance_to_origin(self):
        if len(self.__dict__) < 2:
            return
        else:
            distance = sqrt((self.x)**2 + (self.y)**2)
            return distance
    def display(self):
        if len(self.__dict__) < 2:
            print('Координаты не заданы')
        else:
            print(f'Point({self.x}, {self.y})')
    def get_distance(self, s_self):
        if  isinstance(s_self, Point):
            if hasattr(self, ('x' and 'y')) and hasattr(s_self, ('x' and 'y')):
                return sqrt((self.x - s_self.x) ** 2 + (self.y - s_self.y) ** 2)
            else:
                print('Координаты не заданы')
        else:
            print("Передана не точка")

p1 = Point()
p2 = Point()
print(p1.get_distance(p2))
p1.set_coordinates(1, 2)
print(p1.get_distance(p2))
p2.set_coordinates(4, 6)
assert p1.get_distance(p2) == 5.0    #Практиковался с проверкой, вместо print()
print(p1.get_distance(p2))