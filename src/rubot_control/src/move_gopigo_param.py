#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def odom_callback(data):
    data_odom=data.pose.pose.position.x
    print data_odom
    rospy.loginfo("Robot Odometry x= %f\n",data_odom)

def move_rubot(lin_vel,ang_vel):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom',Odometry, odom_callback)
    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('rubot_control', anonymous=False) # init node has to be made before param.get
        v= rospy.get_param("~v") # ~ because param is inside node in launchfile 
        w= rospy.get_param("~w") # this is important to distinguish the different robots
        move_rubot(v,w)
    except rospy.ROSInterruptException:
        pass