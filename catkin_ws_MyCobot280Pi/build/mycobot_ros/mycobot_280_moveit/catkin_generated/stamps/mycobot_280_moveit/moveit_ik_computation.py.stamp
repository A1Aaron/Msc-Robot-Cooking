#!usr/bin/python
# -*- coding: utf-8 -*-
import rospy, sys
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from copy import deepcopy
from pymycobot import MyCobot
 
 
class MoveItIkDemo:
    def __init__(self):
 
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        
        # 初始化ROS节点
        rospy.init_node('moveit_ik_demo')
                
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm_group')
 
        arm.set_end_effector_link('joint6_flange')
                
        # 获取终端link的名称，这个在setup assistant中设置过了
        end_effector_link = arm.get_end_effector_link()
                        
        # 设置目标位置所使用的参考坐标系
        # reference_frame = 'base_link'
        reference_frame = 'joint1'
        arm.set_pose_reference_frame(reference_frame)
                
        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)
        
        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        arm.set_goal_position_tolerance(0.001)
        arm.set_goal_orientation_tolerance(0.01)
       
        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)
 
        arm.remember_joint_values('home',[0,0,0,0,0,0])
 
        # 控制机械臂先回到初始化位置
        mc.set_gripper_state(0, 70)
        rospy.sleep(3)
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)
               
        # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
        # 姿态使用四元数描述，基于base_link坐标系
        target_pose = PoseStamped()
        #参考坐标系，前面设置了
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now() #时间戳？
        #末端位置   
        target_pose.pose.position.x = 0.184892
        target_pose.pose.position.y = 0.0788132
        target_pose.pose.position.z = 0.1199491
        #末端姿态，四元数
        target_pose.pose.orientation.x = 0.202164
        target_pose.pose.orientation.y = 0.662784
        target_pose.pose.orientation.z = 0.652578
        target_pose.pose.orientation.w = -0.306577
        
        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径，返回虚影的效果
        plan_success, traj, planning_time, error_code = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
 
        waypoints = []
        start_pose = arm.get_current_pose(end_effector_link).pose
        waypoints.append(start_pose)
        wpose = deepcopy(start_pose)#拷贝对象
        wpose.position.z -= 0.065
        waypoints.append(wpose)
 
        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        fraction = 0.0
        maxtries = 100   #最大尝试规划次数
        attempts = 0
 
        while fraction < 1.0 and attempts < maxtries:
        #规划路径 ，fraction返回1代表规划成功
            (plan, fraction) = arm.compute_cartesian_path (
                                    waypoints,   # waypoint poses，路点列表，这里是5个点
                                    0.01,        # eef_step，终端步进值，每隔0.01m计算一次逆解判断能否可达
                                    0.0,         # jump_threshold，跳跃阈值，设置为0代表不允许跳跃
                                    True)        # avoid_collisions，避障规划
            
            # 尝试次数累加
            attempts += 1
            
            # 打印运动规划进程
            if attempts % 10 == 0:
                rospy.loginfo("Still trying after " + str(attempts) + " attempts...")
                     
        # 如果路径规划成功（覆盖率100%）,则开始控制机械臂运动
        if fraction == 1.0:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            arm.execute(plan)
            rospy.loginfo("Path execution complete.")
        # 如果路径规划失败，则打印失败信息
        else:
            rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(maxtries) + " attempts.")  
 
 
        rospy.sleep(1)  #执行完成后休息1s
        mc.set_gripper_state(1, 70)
        rospy.sleep(3)
 
 
        # 控制机械臂回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(3)
 
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
 
if __name__ == "__main__":
    port = rospy.get_param("~port", "/dev/ttyACM0")
    baud = rospy.get_param("~baud", 115200)
    mc = MyCobot(port, baud)
    MoveItIkDemo()
    rospy.spin()