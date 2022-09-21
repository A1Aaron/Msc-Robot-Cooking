import numpy as np
from numpy import load
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from scipy.spatial.transform import Rotation as R
import cv2


R_G2B = []
R_C2T = []
T_G2B = []
T_C2T = []



robotpose = np.load('posearray.npy')
camposeT = np.load('charucoposeT.npy')
camposeR = np.load('charucoposeR.npy')

for x in range(int(np.size(robotpose)/7)):
    
    rx,ry,rz = euler_from_quaternion(robotpose[x][3:])
    print ([rx, ry,rx])
    print("")
    

    rcam = R.from_euler('xyz',camposeR[x].T,degrees=False)
    rcam = rcam.as_matrix()
    rcam = rcam[0]
    tcam = camposeT[x]
    print ("CAMERA")
    print(rcam)
    print(tcam)
    print("") 

    
    rgrip = R.from_euler('xyz',[[rx,ry,rz]],degrees=False)
    rgrip = rgrip.as_matrix()
    rgrip = rgrip[0]
    tgrip = np.array([robotpose[x][0:3]]).T*1000
    print("ROBOT")
    print (rgrip)
    print(tgrip)
    print("")
    
    
    # rcam,rj = cv2.Rodrigues(camposeR[x].T)
    # tcam = camposeT[x]
    # print ("CAMERA")
    # print(rcam)
    # print(tcam)
    # print("") 
  
    # rgrip,rj = cv2.Rodrigues(np.array([rx,ry,rz]))
    # tgrip = np.array([robotpose[x][0:3]]).T*1000
    # print ("ROBOT")
    # print(rgrip)
    # print(tgrip)
    # print("") 
    
   
    
    # Changes B2G to G2B
    rgrip = rgrip.T 
    tgrip = np.matmul(-rgrip,tgrip)
    
    R_G2B.append(rgrip)
    T_G2B.append(tgrip)

    R_C2T.append(rcam)
    T_C2T.append(tcam)




rcalib, tcalib = cv2.calibrateHandEye(R_G2B,T_G2B,R_C2T,T_C2T,method=cv2.CALIB_HAND_EYE_PARK)

print("{} data points used for calibration".format(np.shape(R_G2B)[0]))
print("")
print("CALIB")
print(rcalib)
print(tcalib)
print("")
calib = np.concatenate([rcalib,tcalib],axis = 1)
print(calib)
np.save("calib",calib)


