import visualize as vis
# import a_star_nh_ankur_aditya as astr
import time

if __name__ == "__main__":
    start_time = time.time()
    print("-----------------------")
    print("Path Planning: A star Turtlebot3") 
    print("-----------------------")
    x, y, th = [float(x) for x in input("Enter the Start Coordinates: ").split()] 
    
    if not (0 <= x < 6) or not (0 <= y < 2) or not (0 <= th < 360 and th % 30 == 0):
        raise ValueError("Start coordinates are not acceptable")
    
    x = 0.5 + x
    y = 1 - y

    start = (x,y, th)

    x, y, th = [float(x) for x in input("Enter the Goal Coordinates: ").split()] 
    if not (0 <= x < 6) or not (0 <= y < 2) or not (0 <= th < 360 and th % 30 == 0):
        raise ValueError("Goal coordinates are not acceptable")
    
    x = x + 0.5
    y = 1 - y
    goal = (x,y, th)

    cl = float(input("Enter a Clearance value: "))
    
    rpm_1, rpm_2 = [int(x) for x in input("Enter rpm_1 and rpm_2 : ").split()] 
    if not (0 <= rpm_1 <= 250) or not(0 <= rpm_2 <= 250):
        raise ValueError("Wheel RPM is not acceptable")
    
    scaled_val = 200
    
    root, canvas = vis.main(start,goal,cl,scaled_val)
    # astr.main(root, canvas, start, goal,rpm_1,rpm_2)

    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime: {:.4f} seconds".format(runtime),"\n\n")
    root.mainloop()
