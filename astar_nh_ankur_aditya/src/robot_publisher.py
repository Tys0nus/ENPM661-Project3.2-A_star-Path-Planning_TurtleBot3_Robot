#! /usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

def read_path(filename='track.txt'):
    track = []
    with open(filename, 'r') as f:
        tuples_list = [(float(line.split()[0]), float(line.split()[1])) for line in f]
        track.append(tuples_list)
    return track

def curOrient(msg):
    global ori_x, ori_y, ori_yaw
    ori_x= msg.pose.pose.position.x
    ori_y = msg.pose.pose.position.y
    quat = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
        	msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    _, _, ori_yaw = euler_from_quaternion(quat)

def traverse(x, y):
	twist=Twist()
	pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
	rate = rospy.Rate(10)
	checkGoal = False

	while not checkGoal and not rospy.is_shutdown():
		dx = x - ori_x
		dy = y - ori_y
		t_ang = math.atan2(dy, dx)
		distTar = math.sqrt(dx**2 + dy**2)
	
		if abs(t_ang  - ori_yaw) > 0.1:
			twist.linear.x = 0.0
			twist.angular.z = t_ang  - ori_yaw

		else:
			twist.linear.x = min(0.2, distTar)
			twist.angular.z = 0.0

			if distTar < 0.2:
				checkGoal = True
				twist.linear.x = 0.0
				twist.angular.z = 0.0

		pub.publish(twist)
		rate.sleep()

def test(track_info):
	rospy.init_node('tbot_opencontrol',anonymous=True)
	rospy.Subscriber('/odom', Odometry, curOrient)
	print(track_info)

	for node in track_info:
		traverse(node[0], node[1])
	
if __name__=='__main__':
	global checkGoal
	checkGoal = False
	ori_x= 0.0
	ori_y = 0.0
	ori_yaw = 0.0
	track_info_o = read_path()
	track_info = track_info_o[0]

	test(track_info)

	rospy.sleep()

	
