#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def goal_publisher():
    rospy.init_node('goal_publisher', anonymous=True)
    pub = rospy.Publisher('goal', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Here you will wait for user input on the terminal, in the format
        # x y theta, where x and y are the Cartesian coordinates of the position,
        # and theta is the orientation in radians.
        # You should then publish the start and goal positions as Twist messages
        # on the start and goal topics, respectively.
        x, y, theta = map(float, raw_input('Enter start and goal positions in the format x y theta: ').split())
        start_msg = Twist()
        start_msg.linear.x = x
        start_msg.linear.y = y
        start_msg.angular.z = theta
        pub.publish(start_msg)
        goal_msg = Twist()
        goal_msg.linear.x = x
        goal_msg.linear.y = y
        goal_msg.angular.z = theta
        pub.publish(goal_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        goal_publisher()
    except rospy.ROSInterruptException:
        pass
