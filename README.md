# A-star for Non-holonomic Constraints
This project implements the A* algorithm for finding the optimal path for a robot with non-holonomic constraints. The robot in this project uses differential drive constraints and has 8 action sets for movement.

# Overview
The project implements the A* algorithm to find the optimal path between the start node and the goal node for a robot with non-holonomic constraints. The project uses Python programming language and tkinter GUI for visualization purposes.

# Implementation
The implementation involves defining the state space of the robot and the possible actions it can take. The state space is defined by the position and orientation of the robot, while the actions are defined by the differential drive constraints of the robot. The A* algorithm is then used to find the optimal path between the start and goal nodes, taking into account the non-holonomic constraints of the robot.

# Results
The project provides a visualization of the exploration of nodes during the A* algorithm and the final optimal path of the robot from start node to goal node. The visualization uses the tkinter GUI to plot the nodes and the path on a 2D plane.

# Getting Started
To get started with the project, you will need to have Python installed on your system. You will also need to install the tkinter, math, heapq and numpy libraries. You can clone the repository and run the main.py file to see the visualization of the A* algorithm and the optimal path.

# Contributing
Contributions to the project are welcome. If you find any issues or want to make improvements to the code, feel free to submit a pull request.
