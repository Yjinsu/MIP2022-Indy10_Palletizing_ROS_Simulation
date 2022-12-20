#!/usr/bin/env python
#-*- coding:utf-8 -*- 
import rospy
from indy_driver.msg import TargetPose, IndyRobotState, GripState, GripCommand


robotState = 0
gripState = 0
gripChage = 0
def readRobotState(_msg):
    global robotState
    robotState = _msg.move

def readGripState(_msg):
    global gripState, gripChage
    gripChange = _msg.change
    gripState = _msg.on 

def main():
    
    rospy.init_node('command', anonymous=True)

    pub_TargetPose      = rospy.Publisher("TargetPose", TargetPose, queue_size = 10)
    pub_GripCommand     = rospy.Publisher("GripCommand", GripCommand, queue_size = 10)
    pub_GripState       = rospy.Publisher("GripState", GripState, queue_size = 10)
    sub_IndyRobotState  = rospy.Subscriber("IndyRobotState", IndyRobotState, readRobotState)
    sub_GripState       = rospy.Subscriber("GripState", GripState, readGripState)

    msg_TargetPose  = TargetPose()
    msg_GripCommand = GripCommand()
    msg_GripState   = GripState()
    msg_GripCommand.DO_Pin0 = 10    # Gripper : DO PIN - 8, 9
    msg_GripCommand.DO_Pin1 = 11    # Vaccum  : DO PIN - 10, 11
    msg_GripCommand.DO_Val0 = 0
    msg_GripCommand.DO_Val1 = 1

    cnt = 0
    mode = 0

    loop = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        
        if robotState == 0:     # 로봇이 정지한 상황일 때, count++
            cnt += 1

        if cnt > 90:
            mode = 0
            cnt = 0
        elif cnt > 70:
            mode = 3
            msg_GripState.change = 1
            # cnt = 0

        elif cnt > 40:
            mode = 2

        elif cnt > 30:
            mode = 1
            msg_GripState.change = 1

        if mode == 0:
            msg_TargetPose.x = 0.0
            msg_TargetPose.y = 0.5

        elif mode == 1:
            msg_GripCommand.DO_Val0 = 1
            msg_GripCommand.DO_Val1 = 0
            pub_GripCommand.publish(msg_GripCommand)
            pub_GripState.publish(msg_GripState)

        elif mode == 2:
            msg_TargetPose.x = 0.4
            msg_TargetPose.y = 0.5

        elif mode == 3:
            msg_GripCommand.DO_Val0 = 0
            msg_GripCommand.DO_Val1 = 1
            pub_GripCommand.publish(msg_GripCommand)
            pub_GripState.publish(msg_GripState)

        msg_TargetPose.z        = 0.700
        msg_TargetPose.roll     = 179.9
        msg_TargetPose.pitch    = 0.0
        msg_TargetPose.yaw      = 0.0
    
        pub_TargetPose.publish(msg_TargetPose)
        print("count: " + str(cnt) + " mode: " + str(mode) + " robot state: " + str(robotState))        
        loop.sleep()


    rospy.spin()

if __name__ == '__main__':
    main()
