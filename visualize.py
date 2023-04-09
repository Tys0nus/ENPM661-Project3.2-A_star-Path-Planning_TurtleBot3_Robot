import numpy as np
import tkinter as tk
import math

global robot_radius
robot_radius = 0.105

def points(node):
    x,y,th = node
    r = 5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    pts = [x0,y0,x1,y1]
    return pts

def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='blue')
    return pts

def polygon(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    canvas.create_polygon(pts, fill='blue')
    return pts

def squircles(canvas, points, corner_radius, **kwargs):
    num_points = len(points)

    angles = []
    for i in range(num_points):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%num_points]
        dx, dy = x2-x1, y2-y1
        angles.append(math.atan2(dy, dx))
    
    poly_points = []
    for i in range(num_points):
        x, y = points[i]
        angle1 = angles[i-1]
        angle2 = angles[i]
        dx1, dy1 = corner_radius*math.cos(angle1), corner_radius*math.sin(angle1)
        dx2, dy2 = corner_radius*math.cos(angle2), corner_radius*math.sin(angle2)
        x1, y1 = x-dx1, y-dy1
        x2, y2 = x+dx2, y+dy2
        poly_points.extend([x1, y1, x, y, x2, y2])
    
    return canvas.create_polygon(poly_points, **kwargs, smooth=True)
    
def main(start, goal, clearance,scaled_val=1):
    clearance = clearance
    radius = robot_radius
    distance = clearance + radius

    cr = 0.05 #Fillet radius

    root = tk.Tk()

    global wd, ht, canvas
    wd = 6
    ht = 2

    canvas = tk.Canvas(root, width=wd, height=ht,background='white')
    canvas.pack()

    left_wall = [0, 2, 0, 0, distance, 0, distance, 2]
    right_wall = [6 - distance, 2, 600 - distance, 0, 6, 0, 6, 2]
    upper_wall = [0, distance, 0, 0, 6, 0, 6, distance]
    bottom_wall = [0, 2, 0, 2 - distance, 6, 2 - distance, 6, 2]

    canvas.create_polygon(left_wall, fill='orange')    # left wall
    canvas.create_polygon(right_wall, fill='orange')   # right wall
    canvas.create_polygon(upper_wall, fill='orange')   # upper wall
    canvas.create_polygon(bottom_wall, fill='orange')  # bottom wall

    rect_obs1_c = [(1.5 - distance, 0 - distance), (1.5 - distance, 1.25 + distance), (1.65 + distance, 1.25 + distance), (1.65 + distance, 0 - distance)]
    rect_obs2_c = [(2 - distance, 0.75 - distance), (2.5 - distance, 2 + distance), (2.65 + distance, 2 + distance), (2.65 + distance, 0.75 - distance)]

    squircles(canvas,rect_obs1_c,cr,fill='orange') # Inflated Obs 1
    squircles(canvas,rect_obs2_c,cr,fill='orange') # Inflated Obs 2

    rect_obs1 = [150, 0, 150, 125, 165, 125, 165, 0]
    rect_obs2 = [250, 75, 250, 200, 265, 200, 265, 75]

    canvas.create_polygon(rect_obs1, fill='blue')
    canvas.create_polygon(rect_obs2, fill='blue')

    center_x, center_y = 4, 0.9
    radius = 0.5

    x0 = center_x - radius
    y0 = center_y - radius
    x1 = center_x + radius
    y1 = center_y + radius

    canvas.create_oval(x0 - distance, y0 - distance, x1 + distance, y1 + distance, fill="orange",outline="orange")   # inflated circle
    canvas.create_oval(x0, y0, x1, y1, fill="blue",outline='blue')   

    return root, canvas

if __name__ == "__main__":
    main()



    




    
