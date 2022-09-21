import numpy as np
import time
from numpy import load 
from pymycobot import MyCobot, PI_BAUD, PI_PORT

def start():
    
    def main():
        global start
        global j1data
        global j2data
        global j3data
        global j4data
        global j5data
        global j6data
        global x
        
        while(True):
            if time.time()-start > j1data[x][0]:
                print("Data Reads: {}   Time Reads   {}".format( j1data[x][0], (time.time()-start) ))
                
                if j1data[x][1] >= 180:
                    j1data[x][1] = 180
                elif j1data[x][1] <= -180:
                    j1data[x][1] = -180    
                
                if j2data[x][1] >= 142:
                    j2data[x][1] = 142
                elif j2data[x][1] <= -142:
                    j2data[x][1] = -142     
                
                if j3data[x][1] >= 152:
                    j3data[x][1] = 152
                elif j3data[x][1] <= -155:
                    j3data[x][1] = -155   
                
                if j4data[x][1] >= 150:
                    j4data[x][1] = 150
                elif j4data[x][1] <= -134:
                    j4data[x][1] = -134   
                    
                if j5data[x][1] >= 130:
                    j5data[x][1] = 130
                elif j5data[x][1] <= -166:
                    j5data[x][1] = -166    
                
                if j6data[x][1] >= 180:
                    j6data[x][1] = 180
                elif j6data[x][1] <= -180:
                    j6data[x][1] = -180       
                    
                mc.send_angles([j1data[x][1],j2data[x][1],j3data[x][1],j4data[x][1],j5data[x][1],j6data[x][1]],20)
                x+=1
                
                
            
    def begin():
        global start
        global j1data
        global j2data
        global j3data
        global j4data
        global j5data
        global j6data
        global x
        
        
        x = 1 
        j1data = load ("/shared/j1trajPLACE_TEA.npy")
        j2data = load ("/shared/j2trajPLACE_TEA.npy")
        j3data = load ("/shared/j3trajPLACE_TEA.npy")
        j4data = load ("/shared/j4trajPLACE_TEA.npy")
        j5data = load ("/shared/j5trajPLACE_TEA.npy")
        j6data = load ("/shared/j6trajPLACE_TEA.npy")
        start = time.time()
        
        main()


    # if __name__ == '__main__':
    mc = MyCobot(PI_PORT,PI_BAUD)
    try:
        time.sleep(3)
        begin()  
    except:
        mc.set_gripper_state(0,50)
        import dmp5
        dmp5.start()