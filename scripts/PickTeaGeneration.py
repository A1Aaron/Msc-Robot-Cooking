"""
Copyright (C) 2016 Travis DeWolf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from tkinter import TRUE
import numpy as np
import matplotlib.pyplot as plt

import pydmps
import pydmps.dmp_discrete

def main(target,graph):
    goal = np.load("/home/aaron/catkin_ws/src/mycobot/data/angleGoal.npy")
    goal = goal * 180/np.pi
    goal = np.round(goal,0)
    print("PICK TEA")
    add = 0
    num = 50000
    xLim = 80
    cobot = False
    ######################################### JOINT ONE #####################################################

    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j1trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)

    dmp.imitate_path(y_des=y_des)

    plt.figure(1, figsize=(6, 6))

    y_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y_track[:, 0], y_track[:, 1], "b--", lw=2, alpha=0.5)
    
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[0]]) 
        y_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y_track.append(np.copy(y))
        y_track = np.array(y_track)
        plt.title("DMP system - J1 / Goal {} / Reached {}".format(goal[0],y_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y_track.append(np.copy(y))
        y_track = np.array(y_track)
        plt.title("DMP system - J1 / Goal (Recorded) {}".format(y_des[-1][-1]))    
    

    plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0, xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees")

    ####################################### JOINT TWO #####################################################

    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j2trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)

    dmp.imitate_path(y_des=y_des)
    
    plt.figure(2, figsize=(6, 6))

    y2_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y2_track[:, 0], y2_track[:, 1], "b--", lw=2, alpha=0.5)
    
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[1]]) 
        y2_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y2_track.append(np.copy(y))
        y2_track = np.array(y2_track)
        plt.title("DMP system - J2 / Goal {} / Reached {}".format(goal[1],y2_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y2_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y2_track.append(np.copy(y))
        y2_track = np.array(y2_track)
        plt.title("DMP system - J2 / Goal (Recorded) {}".format(y_des[-1][-1])) 
     

    plt.plot(y2_track[:, 0], y2_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0, xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees")

    #################################### JOINT THREE ###############################################

    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j3trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)
    
    dmp.imitate_path(y_des=y_des)
   
    plt.figure(3, figsize=(6, 6))

    y3_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y3_track[:, 0], y3_track[:, 1], "b--", lw=2, alpha=0.5)
    
     
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[2]]) 
        y3_track = []
        dmp.reset_state()
        for t in range(int(dmp.timesteps+add)):
            y, _, _ = dmp.step()
            y3_track.append(np.copy(y))
        y3_track = np.array(y3_track)
        plt.title("DMP system - J3 / Goal {} / Reached {}".format(goal[2],y3_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y3_track = []
        dmp.reset_state()
        for t in range(int(dmp.timesteps+add)):
            y, _, _ = dmp.step()
            y3_track.append(np.copy(y))
        y3_track = np.array(y3_track)
        plt.title("DMP system - J3 / Goal (Recorded) {}".format(y_des[-1][-1]))  
            
   
    plt.plot(y3_track[:, 0], y3_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0,xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees") 

    ############################################ JOINT FOUR ##############################

    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j4trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)

    dmp.imitate_path(y_des=y_des)

    plt.figure(4, figsize=(6, 6))

    y4_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y4_track[:, 0], y4_track[:, 1], "b--", lw=2, alpha=0.5)
   
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[3]]) 
        y4_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y4_track.append(np.copy(y))
        y4_track = np.array(y4_track)
        plt.title("DMP system - J4 / Goal {} / Reached {}".format(goal[3],y4_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y4_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y4_track.append(np.copy(y))
        y4_track = np.array(y4_track)
        plt.title("DMP system - J4 / Goal (Recorded) {}".format(y_des[-1][-1]))  
        

    plt.plot(y4_track[:, 0], y4_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0, xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees") 

    #################################### JOINT FIVE ################################################


    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j5trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)

    dmp.imitate_path(y_des=y_des)

    plt.figure(5, figsize=(6, 6))

    y5_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y5_track[:, 0], y5_track[:, 1], "b--", lw=2, alpha=0.5)
   
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[4]]) 
        y5_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y5_track.append(np.copy(y))
        y5_track = np.array(y5_track)
        plt.title("DMP system - J5 / Goal {} / Reached {}".format(goal[4],y5_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y5_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y5_track.append(np.copy(y))
        y5_track = np.array(y5_track)
        plt.title("DMP system - J5 / Goal (Recorded) {}".format(y_des[-1][-1]))   
        

    plt.plot(y5_track[:, 0], y5_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0, xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees") 

    ###################################### JOINT SIX ####################################################


    y_des = np.load("/home/aaron/catkin_ws/src/mycobot/data/j6trajPICK_TEA.npy").T

    y_des -= y_des[:, 0][:, None]

    # test normal run
    dmp = pydmps.dmp_discrete.DMPs_discrete(n_dmps=2, n_bfs=num, ay=np.ones(2) * 10.0)

    dmp.imitate_path(y_des=y_des)

    plt.figure(6, figsize=(6, 6))

    y6_track, dy_track, ddy_track = dmp.rollout()
    plt.plot(y6_track[:, 0], y6_track[:, 1], "b--", lw=2, alpha=0.5)
    
    if target == True:
        dmp.goal = np.array([y_des[0][-1], goal[5]]) 
        y6_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y6_track.append(np.copy(y))
        y6_track = np.array(y6_track)
        plt.title("DMP system - J6 / Goal {} / Reached {}".format(goal[5],y6_track[-1][-1]))
    else:
        dmp.goal = np.array([y_des[0][-1],y_des[1][-1]])
        y6_track = []
        dmp.reset_state()
        for t in range(dmp.timesteps+add):
            y, _, _ = dmp.step()
            y6_track.append(np.copy(y)) 
        y6_track = np.array(y6_track)
        plt.title("DMP system - J6 / Goal (Recorded) {}".format(y_des[-1][-1])) 
         

    plt.plot(y6_track[:, 0], y6_track[:, 1], "b", lw=2)
    # plt.axis("equal")
    plt.xlim([0, xLim])
    plt.ylim([-180, 180])
    plt.legend(["original path", "moving target"])
    plt.xlabel("Duration / seconds")
    plt.ylabel("Angle / degrees") 

   

    # print("###############J1###############################")
    # print(y_track)
    # print("###############J2###############################")
    # print(y2_track)
    # print("###############J3###############################")
    # print(y3_track)
    # print("###############J4###############################")
    # print(y4_track)
    # print("###############J5###############################")
    # print(y5_track)
    # print("###############J6###############################")
    # print(y6_track)
    if cobot == True:
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j1trajPICK_TEA',y_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j2trajPICK_TEA',y2_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j3trajPICK_TEA',y3_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j4trajPICK_TEA',y4_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j5trajPICK_TEA',y5_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=public%20files/j6trajPICK_TEA',y6_track)
    else:
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j1trajPICK_TEA',y_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j2trajPICK_TEA',y2_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j3trajPICK_TEA',y3_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j4trajPICK_TEA',y4_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j5trajPICK_TEA',y5_track)
        np.save('/run/user/1000/gvfs/smb-share:server=ubuntu.local,share=cobotshare/j6trajPICK_TEA',y6_track)
    
    if graph == True:
        plt.show()
  

if __name__ == '__main__':
    main(True,True)