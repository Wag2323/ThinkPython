import math
from structshape import structshape


def create_points(x, y, meshsize):
    """Creates a list of x and y grid points based on the axis lengths and mesh
    size given
    
    x, y, meshsize: some positive number
    """
    xy_loc = []

    x_loc = axis_points(x, meshsize)
    y_loc = axis_points(y, meshsize)

    for i in range(0, len(x_loc)):
        for j in range(0, len(y_loc)):
            xy_loc.append((x_loc[i], y_loc[j]))

    return xy_loc


def axis_points(a_len, meshsize):
    """Creates a list of points along an axis spaced at the mesh size. The mesh
    does differ at the end point to make sure the end point is included
    
    a_len, meshsize: some positive number
    """
    axis_loc = [0]
    axis_div = int(a_len / meshsize)

    for i in range(0, axis_div):
        axis_loc.append(axis_loc[-1] + meshsize)

    # adds or modifies last point to allow it to meet up with the end length
    if axis_loc[-1] < a_len:
        axis_loc.append(a_len)

    if axis_loc[-1] > a_len:
        axis_loc[-1] = a_len

    return axis_loc
    
    
def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx**2 + dy**2)
       

if __name__ == '__main__':

    p = create_points(10, 10.6, .25)
    for item in p:
        print item
    print structshape(p)
