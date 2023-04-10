# A-star for Robot with Non-holonomic Constraints
This project implements the A* algorithm to find the optimal path for a robot with non-holonomic constraints, specifically a differential drive robot with 8 action sets for movement.

# Sim Output:

![](https://github.com/ankurchavan1/A-star_for_non-holonomic_constraints/blob/main/sim_output/sim_2D_viz.gif)

# Part 1:
In Part 1, the A* algorithm is implemented in Python programming language with tkinter GUI for visualization. The visualization shows the exploration of nodes during the algorithm and the final optimal path from start to goal node on a 2D plane.

# Dependencies:

The code requires the following dependencies:

-   Python 3.10
-   Numpy
-   math
-   Tkinter
-   heapq
-   time

# How to run the code:

1.  Clone the repository to your local machine.
2.  Navigate to the repository directory.
3.  Install the necessary dependencies by running `pip install -r requirements.txt`.
4.  Run the `main.py` file using `python main.py` command.
5.  The code will prompt the user for inputs as follows: (All inputs in meters)
    -   Start node coordinates and orientation (as three consecutive values with spaces)
    -   Goal node coordinates and orientation (as three consecutive values with spaces)
    -   Wall clearance
    -   Left wheel RPM and Right Wheel RPM (as two consecutive values with spaces)

  Example Input: Test Case 1

- Enter the Start Coordinates: -0.35 -0.75 90
- Enter the Goal Coordinates: 5.25 -0.75 0
- Enter a Clearance value: 0.005
- Enter rpm_1 and rpm_2: 50 100


6.  Enter the required inputs and press enter.
7.  Wait for the code to execute, as it may take some time to complete.
8.  The result will be displayed as an animation of finding the goal node and visualizing the optimal path.

# Result:
The project provides a clear visualization of the exploration of nodes during the A* algorithm and the final optimal path of the robot from start node to goal node. The tkinter GUI is used to plot the nodes and the path on a 2D plane.

# Result Recording:
2D Visualization - [https://drive.google.com/file/d/1HCuRICbRDp1BVJvZ50LMOgotHLTfFFQ9/view?usp=share_link]

# Part 2:
In Part 2, the A* algorithm is implemented to find the optimal path for the Turtlebot3 burger, which is simulated in Gazebo world using ROS subscriber and publisher.

# Dependencies:

The code requires the following dependencies:

-   Python 3.10 (Numpy, math, Tkinter, heapq, time modules)
-   ROS Noetics
-   Gazebo
-   Turtlebot3 Simulations package 

# How to run the code:

1.  Clone the repository to your local machine.
2.  Navigate to the repository directory.
3.  Install the necessary dependencies.
4.  Change directory to catkin workspace.
5.  Run the main.py file located in part01 folder in another terminal, this will create a track.txt file directly into part02 folder which contains the ROS package.
6.  The main.py file will ask the inputs for star position, goal position, clearance, rpm1 and rpm2. Enter them as instructed in part1.
7.  main.py will output the 2D visualization of node exploration and path finding.
5.  Run ROS core in another terminal.
6.  Run "roslaunch astar_nh_ankur_aditya gazebo.launch"
7.  Run the f"rosrun astar_nh_ankur_aditya robot_publisher.py"ollowing command "rosrun astar_nh_ankur_aditya robot_publisher.py" in another terminal


# Result:
The simulation shows the Turtlebot3 burger moving from a user-defined start position to a goal position using the A* algorithm. The visualization is done in the Gazebo world.

# Result Recording:
Turtlebot3 Visualization - [https://drive.google.com/file/d/1yatLnT_VPhdwq5tWCuoflM3u1mRgJmVH/view?usp=share_link]
