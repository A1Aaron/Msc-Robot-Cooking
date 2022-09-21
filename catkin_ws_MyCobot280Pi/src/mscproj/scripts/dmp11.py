import numpy as np
import time
from numpy import load 
from pymycobot import MyCobot, PI_BAUD, PI_PORT, Angle

def start():
    
    def main():
        global start
        global j4data
        global j5data
        global j6data
        global x
        
        while(True):
            if time.time()-start > j4data[x][0]:
                print("Data Reads: {}   Time Reads   {}".format( j4data[x][0], (time.time()-start) ))
                
                
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
                    
                mc.send_angle(Angle.J4.value,j4data[x][1],20)
                mc.send_angle(Angle.J5.value,j5data[x][1],20)
                mc.send_angle(Angle.J6.value,j6data[x][1],20)
                x+=1
                
                
            
    def begin():
        global start
        global j4data
        global j5data
        global j6data
        global x
        
        
        x = 0 

        j4data = load ("/shared/j4trajSTIR_SPOON.npy")
        j5data = load ("/shared/j5trajSTIR_SPOON.npy")
        j6data = load ("/shared/j6trajSTIR_SPOON.npy")
        start = time.time()
        
        main()


    # if __name__ == '__main__':
    mc = MyCobot(PI_PORT,PI_BAUD)
    try:
        time.sleep(3)
        begin() 
    except:
        mc.set_gripper_state(1,50)
        import dmp12
        dmp12.start()
