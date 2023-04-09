import numpy as np
import tkinter as tk
import math
import heapq as hq
import copy

scale_val = 200
######################
# Thresholds
goal_thr = 0.2
thr = 0.05
goal_thr *= scale_val
thr *= scale_val
#################
# Robot Def
global r 
r = 0.033 
r*= scale_val
global robot_radius
robot_radius = 0.105
robot_radius*= scale_val
global L 
L = 0.160 
L*= scale_val

global dt
dt = 0.1

global rps_1, rps_2
##########################
# Canvas
wd = 6*scale_val
ht = 2*scale_val

shape =(4, 6, 4)

nodes = {}

ol = []
visited = set()

def create_actions(rps_1,rps_2):
    action_list = [[0,rps_1],[rps_1,0],[rps_1,rps_1],[0,rps_2],[rps_2,0],[rps_2,rps_2],[rps_1,rps_2],[rps_2,rps_1]]
    return action_list

def eu_dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def plot_vec(canvas, px,py,x,y,color='red'):
    canvas.create_line(px, py, x, y, fill=color, width=1)

def color_space(root, canvas, x,y):
    items = canvas.find_closest(x, y)
    color = canvas.itemcget(items[0], "fill")
    try:
        rgb_color = root.winfo_rgb(color)
    except tk.TclError:
        # Invalid color, set to default value or handle the error based on your requirement
        rgb_color = "#FFFFFF"  # Default value
    return rgb_color

def next_pos(x_n,y_n,theta_n,omega,vel):
        global dt
        x_n += vel * np.cos(theta_n) * dt
        y_n -= vel * np.sin(theta_n) * dt
        theta_n += omega * dt
        return x_n, y_n, theta_n

global is_hit
is_hit = False

def plot_curve(root, canvas, x_i,y_i,theta_i,UL,UR,isplot,color=None):
    t = 0
    global r, L, dt
    x_n = x_i
    y_n = y_i
    theta_n = np.deg2rad(theta_i)
    global is_hit
    is_hit = False
    
    omega = (r / L) * (UR - UL)
    vel = 0.5*r * (UL + UR)

    D=0
    while t<1:
        t += dt
        x_0 = x_n 
        y_0 = y_n
        x_n, y_n, theta_n = next_pos(x_n,y_n,theta_n,omega,vel)
        
        if x_n <= 0 and x_n >= wd and y_n <= 0 and y_n >= ht:
            is_hit = True
            return None, None, None, (None,None)
        # print(x_n,y_n, len(ol))
        col = color_space(root, canvas, x_n, y_n)
        if col == (0, 0, 65535) or col == (65535, 42405, 0):
            is_hit = True
            return None, None, None, (None,None)
    
    x_n = x_i
    y_n = y_i
    theta_n = np.deg2rad(theta_i)
    t = 0
    while t<1:
        t += dt
        x_0 = x_n 
        y_0 = y_n
        x_n, y_n, theta_n = next_pos(x_n,y_n,theta_n,omega,vel)

        D += math.sqrt(math.pow((vel * math.cos(theta_n) * dt),2)+math.pow((vel * math.sin(theta_n) * dt),2))
        if isplot:
            plot_vec(canvas,x_0,y_0,x_n,y_n,color)

    new_node = (x_n,y_n)    
    theta_n= np.rad2deg(theta_n)
    return new_node, theta_n , D, (omega,vel)

def within_thr(node, nodes, thr):
    return any(eu_dist(node_pos, node) <= thr for node_pos in nodes.keys())

def explore(root, canvas,node,actions,goal,thr,goal_thr):
    global is_hit
    if node in visited:
        return
    visited.add(node)
    parent = node
    exp = nodes[parent]
    th = exp[0]
    for action_idx,action in enumerate(actions):
        # if is_hit:
        #     continue
        new_node, new_th, D, (omega,vel) = plot_curve(root, canvas, node[0], node[1], nodes[node][0], UL=action[0], UR=action[1],isplot=True,color='white')
        if new_node == None:
            continue

        pos, ori, c2c_path = new_node, new_th, D
        if pos[0] >= 0 and pos[0] < wd and pos[1] >= 0 and pos[1] < ht:
            c2c = exp[1] + c2c_path 
            if pos in nodes.keys() and c2c >= nodes[pos][1]:
                continue
            c2g = eu_dist(pos, g_pos)
            tc = c2c + c2g 
            if pos not in nodes.keys() or tc < nodes[pos][3]:
                bool_chk = within_thr(pos,nodes,thr)
                if bool_chk == True:
                    continue
                nodes[pos] = (ori, c2c, c2g, tc, parent,action_idx,(omega,vel)) #action of parent            
                if pos not in [n[1] for n in ol]:
                    hq.heappush(ol, (tc, new_node))
                    if eu_dist(pos,goal)<goal_thr:
                        return

def animate(root,canvas, nodes,actions):
    batch = 100 
    node_list = list(nodes.items())
    num_batch = len(node_list) // batch + 1
    for i in range(num_batch):
        chunk = node_list[i*batch:(i+1)*batch]
        for pos, (ori, c2c, c2g, tc, parent,action_idx,(omega,vel)) in chunk:
            if parent is not None:
                px, py = parent[0], parent[1]
                p_theta = nodes[parent][0]
                x, y = pos[0], pos[1]
                act = actions[action_idx]
                plot_curve(root,canvas, px, py,p_theta,act[0],act[1],isplot=True,color='yellow')               
        canvas.after(10)
        canvas.update()       

def tracking(nodes, start, end_node):
    track = []
    node = end_node
    while node is not None:
        track.append(node)
        node = nodes[node][4]
    track.reverse()
    return track

def publish(nodes, start, end_node):
    track_info = []
    node = end_node
    while node is not None:
        omega,vel = (nodes[node][6])
        if omega is not None and vel is not None:
            vel = vel/scale_val
            pack = (omega,vel)
            track_info.append(pack)
        node = nodes[node][4]
            
    track_info.reverse()
    return track_info

def track_animate(root,canvas,track,actions):
    for i in range(len(track)-1):
        node1 = track[i]
        node2 = track[i+1]
        action_chk = nodes[node2][5]
        act = actions[action_chk]
        plot_curve(root,canvas, node1[0], node1[1], nodes[node1][0], UL=act[0], UR=act[1],isplot=True,color='green')

def wheel_l_coords(x,y,theta):
    global r,L
    x1,y1 = x-(0.5*L*np.sin(theta))-(r*np.cos(theta)),y-(0.5*L*np.cos(theta))+(r*np.sin(theta))
    x2,y2 = x-(0.5*L*np.sin(theta))+(r*np.cos(theta)),y-(0.5*L*np.cos(theta))-(r*np.sin(theta))
    return x1,y1,x2,y2

def wheel_r_coords(x,y,theta):
    global r,L
    x1,y1 = x+(0.5*L*np.sin(theta))-(r*np.cos(theta)),y+(0.5*L*np.cos(theta))+(r*np.sin(theta))
    x2,y2 = x+(0.5*L*np.sin(theta))+(r*np.cos(theta)),y+(0.5*L*np.cos(theta))-(r*np.sin(theta))
    return x1,y1,x2,y2

def robot_animate(root,canvas,track,actions, robot_radius):
    radius = robot_radius
    global robot
    global r,L
    global dt

    for i, pos in enumerate(track):
        if i == 0:
            x = pos[0]
            y = pos[1]
            theta = np.deg2rad(nodes[pos][0])
            print(x,y,theta)
            xd = x+(radius*np.cos(theta))
            yd = y-(radius*np.sin(theta))
            robot = canvas.create_oval((x - radius), (y - radius), (x + radius), (y + radius),outline='black')
            direction = canvas.create_line(x, y, xd,yd, arrow=tk.LAST, arrowshape=shape, fill='red', width=1)
            x1,y1,x2,y2 = wheel_r_coords(x,y,theta)
            wheel_r = canvas.create_line(x1, y1, x2,y2, fill='black', width=3)
            x1,y1,x2,y2 = wheel_l_coords(x,y,theta)
            wheel_l = canvas.create_line(x1, y1, x2,y2,fill='black', width=3)
            canvas.itemconfig(robot, outline="black")
            canvas.update()
        else:
            node1 = track[i-1]
            node2 = track[i]
            omega,vel = nodes[node2][6]
            x_n = node1[0]
            y_n = node1[1]
            theta_n = np.deg2rad(nodes[node1][0])
            t = 0
            while t<=1:
                t += dt
                old_x = copy.deepcopy(x_n)
                old_y = copy.deepcopy(y_n)
                old_theta = copy.deepcopy(theta_n)
                x_n, y_n, theta_n = next_pos(x_n,y_n,theta_n,omega,vel)
                dx = x_n - old_x
                dy = y_n - old_y
                xd = x_n+(radius*math.cos(theta_n))
                yd = y_n-(radius*math.sin(theta_n))
                canvas.move(robot, dx, dy)
                canvas.coords(direction, x_n, y_n,xd,yd)
                x1,y1,x2,y2 = wheel_r_coords(x_n,y_n,theta_n)
                canvas.coords(wheel_r,x1, y1,x2,y2)
                x1,y1,x2,y2 = wheel_l_coords(x_n,y_n,theta_n)
                canvas.coords(wheel_l,x1, y1,x2,y2)
                canvas.after(50)
                canvas.update()

def main(root, canvas, start, goal, rpm_1,rpm_2):
    global rps_1,rps_2
    rps_1 = rpm_1*2*np.pi/60
    rps_2 = rpm_2*2*np.pi/60
    actions = create_actions(rps_1,rps_2)
    rps_1 = rpm_1*2*np.pi/60
    rps_2 = rpm_2*2*np.pi/60
    global s_pos
    global s_ori
    global g_pos
    global g_ori
    s_pos,s_ori = start[:2],start[-1]
    g_pos,g_ori = goal[:2],goal[-1]
    s_c2c = 0
    s_c2g = eu_dist(s_pos,g_pos)
    s_tc = s_c2c + s_c2g
    nodes[s_pos] = (s_ori,s_c2c,s_c2g,s_tc,None,None, (None,None))
    end_node = None

    hq.heappush(ol,(eu_dist(s_pos,g_pos),s_pos))

    while ol:
        _, node = hq.heappop(ol)
        if eu_dist(node, g_pos) > goal_thr:
            explore(root,canvas,node,actions,goal,thr,goal_thr)
        else:        
            end_node = node
            print("Goal Reached !")
            animate(root, canvas,nodes,actions)
            if end_node is not None:
                track = tracking(nodes,start,end_node)
                track_info = publish(nodes,start,end_node)
                track_animate(root,canvas,track,actions)
                robot_animate(root,canvas,track,actions,robot_radius)
                with open('output.txt', 'w') as file:
                    for idx,tup in enumerate(track_info):
                        if idx>0:
                            line = ' '.join(str(x) for x in tup)
                            file.write(line + '\n')
            break

if __name__ == "__main__":
    main()
