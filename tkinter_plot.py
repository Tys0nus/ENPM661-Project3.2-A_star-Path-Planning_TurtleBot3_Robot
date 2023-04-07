import numpy as np
import tkinter as tk
import math


# Create a window
root = tk.Tk()

wd = 6000
ht = 2500
canvas = tk.Canvas(root, width=wd, height=ht,background='white')
canvas.pack()


shape =(2, 3, 2)

def plot_vec(canvas, px,py,x,y,color='red'):
    # canvas.create_line(px, 250 - py, x, 250 - y, arrow=tk.LAST, arrowshape=shape, fill=color, width=1)
    canvas.create_line(px, 2500 - py, x, 2500 - y, fill=color, width=1)

# Draw a line on the canvas from (50, 50) to (250, 250) with red color
# canvas.create_line(50, 50, 250, 250, fill='red')

plot_vec(canvas, 50, 50, 100, 100, color='red')

rpm1= 5
rpm2= 10

def plot_curve(Xi,Yi,Thetai,UL,UR):
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180


# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes
    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='red')
        
    Thetan = 180 * (Thetan) / 3.14
    return Xn, Yn, Thetan, D

def action_1(Xi,Yi,Thetai,UL,UR):
    UL = 0
    UR = rpm1
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D

def action_2(Xi,Yi,Thetai,UL,UR):
    UL = rpm1
    UR = 0
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D

def action_3(Xi,Yi,Thetai,UL,UR):
    UL = rpm1
    UR = rpm1
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D

def action_4(Xi,Yi,Thetai,UL,UR):
    UL = 0
    UR = rpm2
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D


def action_5(Xi,Yi,Thetai,UL,UR):
    UL = rpm2
    UR = 0
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D


def action_6(Xi,Yi,Thetai,UL,UR):
    UL = rpm2
    UR = rpm2
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D


def action_7(Xi,Yi,Thetai,UL,UR):
    UL = rpm1
    UR = rpm2
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D


def action_8(Xi,Yi,Thetai,UL,UR):
    UL = rpm2
    UR = rpm1
    t = 0
    r = 33
    L = 160
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
        plot_vec(canvas, Xs, Ys, Xn, Yn, color='blue')
        
    Thetan = 180 * (Thetan) / 3.14
    # new_node = (Xn,Yn)
    # tu = Thetan
    # return new_node,tu
    return Xn, Yn, Thetan, D


X0= plot_curve(0,0,45, 0, 0)

for action in [action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8]:
# for action in [action_1]:
    Xi = X0[0]
    Yi = X0[1]
    Thetai = X0[2]
    action(Xi, Yi, Thetai, UL=0, UR=0)

canvas.configure(width=750, height=312)

# canvas.scale('all', 0, 0, 0.125, 0.125)

# Scale down each item on the canvas individually
for item in canvas.find_all():
    canvas.scale(item, 0, 0, 0.125, 0.125)

# Run the window loop
root.mainloop()