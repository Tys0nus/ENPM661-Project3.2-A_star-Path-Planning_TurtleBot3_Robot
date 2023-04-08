#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Twist

def path_publisher_callback(data):
    # Here you will implement your A* algorithm to compute the path
    # between the start and goal positions, and publish it on the path
    # topic as a series of PoseStamped messages.
    pass

def path_publisher():
    rospy.init_node('path_publisher', anonymous=True)
    rospy.Subscriber('start', Twist, path_publisher_callback)
    rospy.Subscriber('goal', Twist, path_publisher_callback)
    pub = rospy.Publisher('path', PoseStamped, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Here you will publish the path as a series of PoseStamped messages
        # on the path topic.
        # Each PoseStamped message should contain the x, y, and theta
        # coordinates of a point on the path.
        # You should publish the messages at a rate of 10Hz.
        rate.sleep()

if __name__ == '__main__':
    try:
        path_publisher()
    except rospy.ROSInterruptException:
        pass
