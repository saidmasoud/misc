#!/usr/bin/python3
'''
Source: CS Dojo https://www.youtube.com/watch?v=eaYX0Ee0Kcg
Objective: given the six points below, find the k nearest
points to the origin.


'''

from math import pow,sqrt
import sys,re

points = [[-2,4],[0,-2],[-1,0],[2,-5],[-2,-3],[3,2]]

num_points = sys.argv[1]

if not re.match(r"[1-6]",num_points):
    print("ERROR: you must specify a number from 1 to 6")
    sys.exit(1)

print("Points to calculate: " + str(points))

# d=sqrt((x2-x1)^2+(y2-y1)^2))

closest = []

for point in points:
    # Since (0,0) is the second point, we can simplify the
    # distance formula calculation
    distance = sqrt(pow(point[0],2)+pow(point[1],2))
    point_obj = {"x":point[0],"y":point[1],"d":distance}
    if len(closest)<int(num_points):
        closest.append(point_obj)
    else:
        for i in range(0,int(num_points)):
            if closest[i]["d"]>point_obj["d"]:
                closest[i] = point_obj
                break

print("Closest points to the origin:")
for point in closest:
    print("({},{}), distance from origin: {}".format(point["x"],point["y"],point["d"]))
