import visualize as vis
import a_star_nh_ankur_aditya as astr
import time

if __name__ == "__main__":
    start_time = time.time()
    print("-----------------------")
    print("Path Planning: A star Turtlebot3") 
    print("-----------------------")
    scaled_val = 200
    x, y, th = [float(x) for x in input("Enter the Start Coordinates: ").split()] 
    
    if not (-0.5 <= x < 5.5) or not (-1 <= y < 1) or not (0 <= th < 360 and th % 15 == 0):
        raise ValueError("Start coordinates are not acceptable")
    
    x = (0.5 + x)*scaled_val
    y = (1 - y)*scaled_val

    start = (x,y, th)

    x, y, th = [float(x) for x in input("Enter the Goal Coordinates: ").split()] 
    if not (-0.5 <= x < 5.5) or not (-1 <= y < 1) or not (0 <= th < 360 and th % 15 == 0):
        raise ValueError("Goal coordinates are not acceptable")
    
    x = (x + 0.5)*scaled_val
    y = (1 - y)*scaled_val
    goal = (x,y, th)

    cl = float(input("Enter a Clearance value: "))
    
    rpm_1, rpm_2 = [int(x) for x in input("Enter rpm_1 and rpm_2 : ").split()] 
    if not (0 <= rpm_1 <= 250) or not(0 <= rpm_2 <= 250):
        raise ValueError("Wheel RPM is not acceptable")

    root, canvas = vis.main(start,goal,cl,scaled_val)
    astr.main(root, canvas, start, goal,rpm_1,rpm_2)

    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime: {:.4f} seconds".format(runtime),"\n\n")
    root.mainloop()
