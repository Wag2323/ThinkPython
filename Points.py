import math
import copy


class Point(object):
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
        
    def __add__(self, other):
        sum = Point()
        sum.x = self.x + other.x
        sum.y = self.y + other.y
        return sum
        

def print_point(p):
    """Print a Point object in readable format."""
    print '(%g, %g)' % (p.x, p.y)
    
    
def distance_between_points(p1, p2):
    """Find the distance between two Point objects"""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx**2 + dy**2)
        
        
class Rectangle(object):
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """
 

def find_center(rect):
    """Find the center of a rectangle object"""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p
    
    
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    

def move_rectangle_copy(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    move_rectangle(new_rect, dx, dy)
    return new_rect

    
if __name__ == '__main__':
    
    # print Point
    # blank = Point()
    # something = Point()
    # print blank
    
    # blank.x = 3.0
    # blank.y = 4.0
    # something.x = 5.0
    # something.y = 6.0
    # d = distance_between_points(blank, something)
    # print d 

    box = Rectangle()
    box.width = 100.1
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    center = find_center(box)
    print_point(center)
    print box.width
    print box.height
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height
    print_point(box.corner)
    move_rectangle(box, 5, 5)
    print_point(box.corner)
    new_box = move_rectangle_copy(box, 20, 20)
    print_point(box.corner)
    print_point(new_box.corner)
    
    # p1 = Point()
    # p1.x = 3.0
    # p1.y = 4.0
    # p2 = copy.copy(p1)
    # print_point(p1)
    # print_point(p2)
    # print p1 is p2
    # print p1 == p2
    # box2 = copy.copy(box)
    # print box2 is box
    # print box2.corner is box.corner
    # box3 = copy.deepcopy(box)
    # print box3 is box
    # print box3.corner is box.corner
    # new_box = move_rectangle_copy(box, 20, 20)
    # print_point(box.corner)
    # print_point(new_box.corner)
    
    w = Point()
    print w
    w = Point(1, 1)
    z = Point(3, 3)
    wz = w + z
    print wz