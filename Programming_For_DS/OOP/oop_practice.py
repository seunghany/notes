# Write two classes Point and Line that give the same output as below:
# >>> line = Line( Point(1, 1), Point(3, 2) )  # a line comprised of two 2D points
# >>> line.slope() 
# 0.5
# >>> line.length()
# 2.23606797749979
import math
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line(Point):
    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def slope(self) -> float:
        '''slope function
         rise/run
        y2-y1/ x2-x1'''
        y2 = self.point_2.y
        y1 = self.point_1.y
        x2 = self.point_2.x
        x1 = self.point_1.x
        line_slope = (y2-y1)/(x2-x1)
        return line_slope

    def length(self) -> float:
        '''
        Find length of the line
        sqrt((y2-y1)^2 + (x2-x1)^2)
        '''
        y2 = self.point_2.y
        y1 = self.point_1.y
        x2 = self.point_2.x
        x1 = self.point_1.x
        line_length = math.sqrt((y2-y1)**2 + (x2-x1)**2) # 픽타고라스
        return line_length

if __name__ == "__main__":
    point1 = Point(1,1)
    point2 = Point(3,2)
    line = Line(point1,point2)
    print("slope: ", line.slope())
    print("length: ",line.length())