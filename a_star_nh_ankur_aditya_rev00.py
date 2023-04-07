import numpy as np
import tkinter as tk
import math
import heapq as hq

def zoom(event):
    if event.delta > 0:
        factor = 1.1
    else:
        factor = 0.9
    
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    canvas.scale("all", x, y, factor, factor)

########################
start = (10,125,90)
goal = (200,125,0)
rpm_1 = 50
rpm_2 = 100
step = 10
########################

root = tk.Tk()
time = [0.1*t for t in range(11) ]
wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht,background='white')
canvas.pack()

shape =(2, 3, 2)

nodes = {}

ol = []
visited = set()

def eu_dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def plot_vec(canvas, px,py,x,y,color='red'):
    canvas.create_line(px, py, x, y, fill=color, width=1)

def color_space(root, canvas, x,y):
    items = canvas.find_closest(x,y)
    color = root.winfo_rgb(canvas.itemcget(items[0], "fill"))
    return color

def plot_curve(canvas, x_i,y_i,theta_i,UL,UR):
    t = 0
    r = 0.038 * 10
    L = 0.354 * 10
    dt = 0.1
    x_n = x_i
    y_n = y_i
    theta_n = np.deg2rad(theta_i)

    D=0
    while t<1:
        t += dt
        x_0 = x_n
        y_0 = y_n
        x_n += 0.5*r * (UL + UR) * math.cos(theta_n) * dt
        y_n -= 0.5*r * (UL + UR) * math.sin(theta_n) * dt
        theta_n += 0.1*(r / L) * (UR - UL) * dt
        plot_vec(canvas,x_0,y_0,x_n,y_n)

    new_node = (x_n,y_n)    
    theta_n= np.rad2deg(theta_n)
    return new_node, theta_n #, D


def explore(canvas,node):
    eu = step
    if node in visited:
        return
    visited.add(node)
    parent = node
    exp = nodes[parent]
    th = exp[0]
    for action in [[0,rpm_1],[rpm_1,0],[rpm_1,rpm_1],[0,rpm_2],[rpm_2,0],[rpm_2,rpm_2],[rpm_1,rpm_2],[rpm_2,rpm_1]]:
        new_node, new_th = plot_curve(canvas, node[0], node[1], nodes[node][0], UL=action[0], UR=action[1])
        pos, ori = new_node, new_th
        if pos[0] >= 0 and pos[0] < wd and pos[1] >= 0 and pos[1] < ht:
            # color = color_space(root, canvas, pos[0], pos[1])
            # if color == (0, 0, 65535) or color == (65535, 42405, 0):
            #     continue
            c2c = exp[1] + eu_dist(parent, pos)
            
            if pos in nodes.keys() and c2c >= nodes[pos][1]:
                continue
            c2g = eu_dist(pos, g_pos)
            tc = c2c + c2g 

            if pos not in nodes.keys() or tc < nodes[pos][3]:
                nodes[pos] = (ori, c2c, c2g, tc, parent)              
                if pos not in [n[1] for n in ol]:
                    hq.heappush(ol, (tc, new_node))
                    if eu_dist(pos,goal)<goal_thr:
                        return

eu =  20
goal_thr = 20
thr = 20
global s_pos, s_ori, g_pos, g_ori

s_pos,s_ori = start[:2],start[-1]
g_pos,g_ori = goal[:2],goal[-1]
s_c2c = 0
s_c2g = eu_dist(s_pos,g_pos)
s_tc = s_c2c + s_c2g
nodes[s_pos] = (s_ori,s_c2c,s_c2g,s_tc,None)
end_node = None

canvas.create_oval(start[0]-5,start[1]-5,start[0]+5,start[1]+5,fill = "green",width = 2)
canvas.create_oval(goal[0]-5,goal[1]-5,goal[0]+5,goal[1]+5,fill = "green",width = 2)
canvas.create_oval(goal[0]-goal_thr,goal[1]-goal_thr,goal[0]+goal_thr,goal[1]+goal_thr,outline='black')

hq.heappush(ol,(eu_dist(s_pos,g_pos),s_pos))

while ol:
    _, node = hq.heappop(ol)
    if eu_dist(node, g_pos) > goal_thr:
        explore(canvas,node)
    else:
        print("Goal Reached")
        break
####################
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
# _, node = hq.heappop(ol)
# explore(canvas,node)
# print(eu_dist(node, g_pos),nodes[node][3])
###################
for item in canvas.find_all():
    canvas.scale(item, 0,0, 1.25,1.25)

canvas.bind("<MouseWheel>", zoom)
root.mainloop()


