# Q no. 7:
# Write a program that receives a list of tuples representing (x, y) coordinates. Determine whether the points form a straight line.

def is_straight_line(points):
    if len(points) < 2:
        return True
    
    x0, y0 = points[0]
    x1, y1 = points[1]
    dx = x1 - x0
    dy = y1 - y0
    
    for i in range(2, len(points)):
        x, y = points[i]
        if (y - y0) * dx != dy * (x - x0):
            return False
    return True

points1 = [(1, 2), (2, 4), (3, 6), (4, 8)]
points2 = [(1, 1), (2, 2), (3, 5)]

print("Points1 form a straight line:", is_straight_line(points1))
print("Points2 form a straight line:", is_straight_line(points2))