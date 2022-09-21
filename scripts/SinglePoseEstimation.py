import os
import cv2
import cv2.aruco as aruco
import numpy as np
import time
from scipy.spatial.transform import Rotation as R
from movecommander2 import plan
import matplotlib.pyplot as plt

initx = 0
inity = 0

SpoonTvec = np.array([[0,0,0]])
BaseTvec = np.array([[0,0,0]])
WaterCupTvec = np.array([0,0,0])
TeaCupTvec = np.array([0,0,0])
WaterCupTvecOff = np.array([0,0,0])
TeaCupTvecOff = np.array([0,0,0])
TeaBagTvec = np.array([[0,0,0]])

SpoonRvec = np.array([[0,0,0]])
BaseRvec = np.array([[0,0,0]])
TeaCupRvec = np.array([[0,0,0]])
WaterCupRvec = np.array([[0,0,0]])
TeaBagRvec = np.array([[0,0,0]])

Ltvecpose = 0
Lrvecpose = 0

errorx =0.83
errory =0.83

TeaBagSeen = False
TeaCupSeen = False
BaseSeen = False
WaterCupSeen = False
SpoonSeen = False
Go = False


# Function to create CharucoBoard with specified marker values
def CharucoBoard(squaresX=7, squaresY=6, squareLength=30, markerLength=22,
                 marker_size=4,total_markers=250):
    
    # Creates a custermizable key in the format arruco.DICT_4X4_1000
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')   
    
    # Fetches stated dictionary using the key        
    arucoDict = aruco.Dictionary_get(key)
    
    # Creates the board object
    Board = aruco.CharucoBoard.create(squaresX,squaresY,squareLength,markerLength,arucoDict)
    
    # Returns Board Image
    return Board

# MakerSize 4X4 MAX MARKERID 1000 with drawing enabled   
def DetectPose(Imgl,draw,marker_size=4,total_markers =250, ):  
   
    global initx
    global inity
    
    global SpoonTvec 
    global SpoonRvec 
    global BaseTvec 
    global BaseRvec
    global WaterCupTvec 
    global WaterCupRvec
    global WaterCupTvecOff
    global TeaCupTvecOff  
    global TeaCupTvec 
    global TeaCupRvec
    global TeaBagTvec 
    global TeaBagRvec
    
    global Ltvecpose 
    global Lrvecpose 
    
    global errorx 
    global errory 
    
    global TeaBagSeen
    global TeaCupSeen
    global WaterCupSeen
    global BaseSeen
    global SpoonSeen
 
    global TeaBagxpos
    global TeaBagypos
    global TeaCupxpos
    global TeaCupypos
    global TeaCupoffxpos
    global TeaCupoffypos
    global WaterCupxpos
    global WaterCupypos
    global WaterCupoffxpos
    global WaterCupoffypos
    global Spoonxpos
    global Spoonypos

    global Go
    
    
    # Converts parsed image to grayscale
    grayl = cv2.cvtColor(Imgl,cv2.COLOR_BGR2GRAY)
    # Creates a custermizable key in the format arruco.DICT_4X4_1000                                        
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')  
    # Fetches stated dictionary using the key       
    arucoDict = aruco.Dictionary_get(key)            
    # Creates detector parameters - default settings                               
    arucoParam = aruco.DetectorParameters_create()       
    # Detecs Markers and Saves corners, IdNumber and rejected markers to variables                          
    markercornersl, idsl, rejectedl = aruco.detectMarkers(grayl, arucoDict, parameters = arucoParam) 
    
    # If markers are detected in left camera
    if len(markercornersl) > 0 :
        # Runs CharucoBoard function to get Board object
        Board = CharucoBoard()
        # Refining detected Markers using the created board object 
        markercornersl, idsl, rejectedl,recoveredidsl = aruco.refineDetectedMarkers(grayl,Board,markercornersl,idsl,rejectedl)
        # Detect CharucoCorners and saves the value detected, corners, and Ids to variables
        retvall, charucoCornersl, charucoIdsl = aruco.interpolateCornersCharuco(markercornersl,idsl,grayl,Board)
        # If more than 25 Charuco board corners are detected
        
        if (retvall>=0):

            # Estimate the pose of the markers
            Lrvecpose, Ltvecpose,objpts = cv2.aruco.estimatePoseSingleMarkers(markercornersl,26,LcameraMatrix, distL,None,None)
            Ltvecpose = np.round(Ltvecpose,2)
            Lrvecpose = np.round(Lrvecpose,2)
            rvec = tvec = np.array([[0],[0],[0]],np.float64)
            
            if Go == False:
                for i in range (np.size(idsl)):
                    
                    ############################### SPOON DETECTION #################################
                    if idsl[i] == 0:
                        
                        Rvec=Lrvecpose[i]
                        Tvec=Ltvecpose[i]
                        
                        Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,Tvec, 50.0,3) 
                        imgpoints = cv2.projectPoints(np.array([[int(Tvec[0][0])],[int(Tvec[0][1])],[int(Tvec[0][2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                        font                   = cv2.FONT_HERSHEY_SIMPLEX
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                        fontScale              = 0.6
                        fontColor              = (0,0,255)
                        thickness              = 2
                        lineType               = 3
                        cv2.putText(Imgl,"Spoon", locationText,font,fontScale,fontColor,thickness,lineType)
                        
                        SpoonTvec = Tvec
                        SpoonTvec[0][0]*=errorx
                        SpoonTvec[0][1]*=errory
                        
                        Spoonxpos = np.round((SpoonTvec[0][0]-BaseTvec[0][0]+60)*-1,2)
                        Spoonypos = np.round((SpoonTvec[0][1]-BaseTvec[0][1])*1,2)
                        
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                        fontScale              = 0.4
                        fontColor              = (255,0,0)
                        cv2.putText(Imgl,"({},  {})".format(Spoonxpos,Spoonypos), locationText,font,fontScale,fontColor,thickness,lineType)
                       
                        SpoonSeen = True
                    
                    
                    ##################################### TEACUP DETECTION #########################
                    if idsl[i] == 1:
                        
                        Rvec=Lrvecpose[i]
                        Tvec=Ltvecpose[i]
                
                        Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,Tvec, 50.0,3) 
                        imgpoints = cv2.projectPoints(np.array([[int(Tvec[0][0])],[int(Tvec[0][1])],[int(Tvec[0][2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                        font                   = cv2.FONT_HERSHEY_SIMPLEX
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                        fontScale              = 0.6
                        fontColor              = (0,0,255)
                        thickness              = 2
                        lineType               = 3
                        cv2.putText(Imgl,"TeaCup", locationText,font,fontScale,fontColor,thickness,lineType)   
                        
                        
                        locationText1 = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                        fontScale              = 0.4
                        fontColor              = (255,0,0)
                    
                        TeaCupTvec=Tvec
                        TeaCupRvec=Rvec
                        
    
                        ## Vector Transformation to get Actual Cup position ##
                        lastrow = np.array([[0,0,0,1]])
                        
                        rC2Wa = R.from_euler('xyz',[[TeaCupRvec[0][0],TeaCupRvec[0][1],TeaCupRvec[0][2]]],degrees=False)
                        rC2Wa = rC2Wa.as_matrix()
                        rC2Wa = rC2Wa[0]
                        TeaCupTvec=np.array(TeaCupTvec).T
                        HC2WA = np.concatenate([rC2Wa,TeaCupTvec],axis=1)
                        HC2WA = np.concatenate([HC2WA,lastrow],axis=0)
                        
                        rT2Cup = np.eye(3)
                        tT2Cup = np.array([[0],[60],[0]]) 
                        HT2Cup = np.concatenate([rT2Cup,tT2Cup],axis=1) 
                        HT2Cup = np.concatenate([HT2Cup,lastrow],axis=0)
                    
                        val = (HC2WA @ HT2Cup)
                        offTvec = np.concatenate([val[:,3][:2], [TeaCupTvec[2][0]]],axis=0)
                        offRvec = R.from_matrix(val[:3,:3])
                        offRvec = offRvec.as_rotvec()
                        offRvec = offRvec
                        
                        if 0.95 < TeaCupTvec[0][0]/offTvec[0] < 1.05:
                            
                            Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,offTvec, 50.0,3) 
                            imgpoints = cv2.projectPoints(np.array([[int(offTvec[0])],[int(offTvec[1])],[int(offTvec[2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                            
                            locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                            fontScale              = 0.6
                            fontColor              = (0,0,255)
                            cv2.putText(Imgl,"TeaCupOffset", locationText,font,fontScale,fontColor,thickness,lineType) 
                            
                            locationText2 = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                            fontScale              = 0.4
                            fontColor              = (255,0,0)
                            
                            TeaCupTvecOff = val[:,3][:3]
                            TeaCupTvecOff[0]*=errorx
                            TeaCupTvecOff[1]*=errory
                            
                            TeaCupoffxpos = np.round((TeaCupTvecOff[0]-BaseTvec[0][0]+60)*-1,2)
                            TeaCupoffypos = np.round((TeaCupTvecOff[1]-BaseTvec[0][1])*1,2)
                            
                            cv2.putText(Imgl,"({},  {})".format(TeaCupoffxpos,TeaCupoffypos), locationText2,font,fontScale,fontColor,thickness,lineType)
                            TeaCupSeen = True
                        
                        TeaCupTvec[0]*=errorx
                        TeaCupTvec[1]*=errory
                        
                        TeaCupxpos = np.round((TeaCupTvec[0][0]-BaseTvec[0][0]+60)*-1,2)
                        TeaCupypos = np.round((TeaCupTvec[1][0]-BaseTvec[0][1])*1,2)
                        
                        cv2.putText(Imgl,"({},  {})".format(TeaCupxpos,TeaCupypos),locationText1,font,fontScale,fontColor,thickness,lineType)
                        
                        
                        
                
                    ################################### WATERCUP DETECTION #########################
                    if idsl[i] == 2:
                        
                        Rvec=Lrvecpose[i]
                        Tvec=Ltvecpose[i]
                        
                        Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,Tvec, 50.0,3) 
                        imgpoints = cv2.projectPoints(np.array([[int(Tvec[0][0])],[int(Tvec[0][1])],[int(Tvec[0][2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                        font                   = cv2.FONT_HERSHEY_SIMPLEX
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                        fontScale              = 0.6
                        fontColor              = (0,0,255)
                        thickness              = 2
                        lineType               = 3
                        cv2.putText(Imgl,"WaterCup", locationText,font,fontScale,fontColor,thickness,lineType) 
                      
                        locationText1 = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                        fontScale              = 0.4
                        fontColor              = (255,0,0)
                        
                        WaterCupTvec = Tvec
                        WaterCupRvec = Rvec
                        
                        
                        # Vector Transformation to get Actual Cup position ##
                        lastrow = np.array([[0,0,0,1]])
                        
                        rC2Wa = R.from_euler('xyz',[[WaterCupRvec[0][0],WaterCupRvec[0][1],WaterCupRvec[0][2]]],degrees=False)
                        rC2Wa = rC2Wa.as_matrix()
                        rC2Wa = rC2Wa[0]
                        WaterCupTvec=np.array(WaterCupTvec).T
                        HC2WA = np.concatenate([rC2Wa,WaterCupTvec],axis=1)
                        HC2WA = np.concatenate([HC2WA,lastrow],axis=0)
                        
                        rT2Cup = np.eye(3)
                        tT2Cup = np.array([[0],[40],[0]]) 
                        HT2Cup = np.concatenate([rT2Cup,tT2Cup],axis=1) 
                        HT2Cup = np.concatenate([HT2Cup,lastrow],axis=0)
                        
                        val = np.matmul(HC2WA,HT2Cup)
                        offTvec = np.concatenate([val[:,3][:2], [WaterCupTvec[2][0]]],axis=0)
                        
                        if  0.95 < WaterCupTvec[0][0]/offTvec[0] < 1.05:
                            Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,offTvec, 50.0,3)         
                            imgpoints = cv2.projectPoints(np.array([[int(offTvec[0])],[int(offTvec[1])],[int(offTvec[2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                            locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                            fontScale              = 0.6
                            fontColor              = (0,0,255)
                            cv2.putText(Imgl,"WaterCupOffset", locationText,font,fontScale,fontColor,thickness,lineType) 
                        
                            locationText2 = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                            fontScale              = 0.4
                            fontColor              = (255,0,0)
                            
                            WaterCupTvecOff = val[:,3][:3]
                            WaterCupTvecOff[0]*=errorx
                            WaterCupTvecOff[1]*=errory
                            
                            WaterCupoffxpos = np.round((WaterCupTvecOff[0]-BaseTvec[0][0]+60)*-1,2)
                            WaterCupoffypos = np.round((WaterCupTvecOff[1]-BaseTvec[0][1])*1,2)
                            
                            cv2.putText(Imgl,"({},  {})".format(WaterCupoffxpos,WaterCupoffypos), locationText2,font,fontScale,fontColor,thickness,lineType)
                            
                            WaterCupSeen = True
                        
                    
                        WaterCupTvec[0]*=errorx
                        WaterCupTvec[1]*=errory
                        
                        WaterCupxpos = np.round((WaterCupTvec[0][0]-BaseTvec[0][0]+60)*-1,2)
                        WaterCupypos = np.round((WaterCupTvec[1][0]-BaseTvec[0][1])*1,2)
                        
                        
                        cv2.putText(Imgl,"({},  {})".format(WaterCupxpos,WaterCupypos), locationText1,font,fontScale,fontColor,thickness,lineType)
                        
                        
                        
                        
                     
                    #################################### TEABAG DETECTION ###########################
                    if idsl[i] == 4:
                        
                        Rvec=Lrvecpose[i]
                        Tvec=Ltvecpose[i]
                        
                        Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,Tvec, 50.0,3) 
                        imgpoints = cv2.projectPoints(np.array([[int(Tvec[0][0])],[int(Tvec[0][1])],[int(Tvec[0][2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                        font                   = cv2.FONT_HERSHEY_SIMPLEX
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                        fontScale              = 0.6
                        fontColor              = (0,0,255)
                        thickness              = 2 
                        lineType               = 3
                        cv2.putText(Imgl,"TeaBag", locationText,font,fontScale,fontColor,thickness,lineType)
                        
                        TeaBagTvec = Tvec
                        TeaBagTvec[0][0]*=errorx
                        TeaBagTvec[0][1]*=errory
                       
                        TeaBagxpos = np.round((TeaBagTvec[0][0]-BaseTvec[0][0]+60)*-1,2)
                        TeaBagypos = np.round((TeaBagTvec[0][1]-BaseTvec[0][1])*1,2)
                        
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                        fontScale              = 0.4
                        fontColor              = (255,0,0)
                        cv2.putText(Imgl,"({},  {})".format(TeaBagxpos,TeaBagypos), locationText,font,fontScale,fontColor,thickness,lineType)
                        
                        TeaBagSeen = True
                        
                    ##################################### BASE DETECTION ############################
                    if idsl[i] == 5:
                        
                        Rvec=Lrvecpose[i]
                        Tvec=Ltvecpose[i]
                    
                        initx = Tvec[0][0]-(60)
                        inity = Tvec[0][1]
                       
                        Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Rvec,Tvec, 50.0,3) 
                        imgpoints = cv2.projectPoints(np.array([[int(Tvec[0][0])],[int(Tvec[0][1])],[int(Tvec[0][2])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
                        
                        font                   = cv2.FONT_HERSHEY_SIMPLEX
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+20)
                        fontScale              = 0.6
                        fontColor              = (0,0,255)
                        thickness              = 2
                        lineType               = 3
                        cv2.putText(Imgl,"Base", locationText,font,fontScale,fontColor,thickness,lineType)
                        
                        locationText = (int(imgpoints[0][0][0][0])+20,int(imgpoints[0][0][0][1])+40)
                        fontScale              = 0.4
                        fontColor              = (255,0,0)
                        cv2.putText(Imgl,"({},  {})".format(np.round((Tvec[0][0]-initx)*-1,2),np.round((Tvec[0][1]-inity)*1),2), locationText,font,fontScale,fontColor,thickness,lineType)
                        
                        BaseTvec = Tvec
                        BaseTvec[0][0]*=errorx
                        BaseTvec[0][1]*=errory
                       
                        BaseSeen = True
                  
                        
                # print("TeaCup: {}\nTeaBag: {}\nBaseSeen: {}".format(TeaCupSeen,TeaBagSeen,BaseSeen))
                

            elif WaterCupSeen == True and TeaCupSeen == True and TeaBagSeen == True and SpoonSeen == True and Go == True and BaseSeen == True: 
                    # Pick WaterCup
                X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose5.npy')
                plt.close('all') 
                print("WATERCUP POS: ({},{})".format(WaterCupoffxpos,WaterCupoffypos))
                plan(WaterCupoffxpos*0.001,WaterCupoffypos*0.001,Z,RX,RY,RZ,5)
                
                # Pick TeaCup
                X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose1.npy')
                # print("TEACUP POS: ({},{})".format(TeaCupoffxpos,TeaCupoffypos))
                plt.close('all') 
                plan(TeaCupoffxpos*0.001,TeaCupoffypos*0.001,Z,RX,RY,RZ,1)
                
            
                # # Place TeaCup
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose2.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,2)

                # Pick TeaBag
                X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose3.npy')
                plt.close('all') 
                print("TEABAG POS: ({},{})".format(TeaBagxpos,TeaBagypos))
                plan(TeaBagxpos*0.001,TeaBagypos*0.001,Z,RX,RY,RZ,3)
                
                # # Place TeaBag
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose4.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,4)
                
             
                
                # # Locate WaterCup
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose6.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,6)
                
                # # Pour WaterCup
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose7.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,7)
                
                # # Place WaterCup
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose8.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,8)
                
                # Pick Spoon
                X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose9.npy')
                plt.close('all') 
                print("SPOON POS: ({},{})".format(Spoonxpos,Spoonypos))
                plan(Spoonxpos*0.001,Spoonypos*0.001,Z,RX,RY,RZ,9)
                
                # # Locate Spoon
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose10.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,10)
                
                # # Stir Spoon
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose11.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,11)
                
                # # Place Spoon
                # X,Y,Z,RX,RY,RZ = np.load('/home/aaron/catkin_ws/src/mycobot/data/pose12.npy')
                # plt.close('all') 
                # plan(X,Y,Z,RX,RY,RZ,12)
                
                Go = False
             
            else:
                objects = []
                if WaterCupSeen == False:
                    objects.append("WaterCup")
                if TeaCupSeen == False:
                    objects.append("TeaCup")
                if SpoonSeen == False:
                    objects.append("Spoon")
                if TeaBagSeen == False:
                    objects.append("TeaBag")
                if BaseSeen == False:
                    objects.append("Base")
                    
                print("Failed to locate the: {} ".format(objects))   
                Go = False
            
            ## USED FOR ERROR CALIBRATION ##
            # print("DISTANCE X")
            # print(initx) 
            # print(BaseTvec[0][0]-TeaCupTvec[0])
            # print(TeaCupTvec[0]-SpoonTvec[0][0])
            # print(SpoonTvec[0][0]-WaterCupTvec[0])
            # print(WaterCupTvec[0]-TeaBagTvec[0][0])
            # print("DISTANCE Y")
            # print(inity)
            # print(BaseTvec[0][1]-TeaCupTvec[1])
            # print(TeaCupTvec[1]-SpoonTvec[0][1])
            # print(SpoonTvec[0][1]-WaterCupTvec[1])
            # print(WaterCupTvec[1]-TeaBagTvec[0][1])
        
    return Imgl

def main():  
    
    
    # Array used to store info from images processed  
    global LcameraMatrix
    global LnewCameraMatrix
    global distL
    global Go
    
    # Opening camera map parameters to undistort and rectify images
    cv_file = cv2.FileStorage()

    # Opends camera calibration parameters
    cv_file.open('/home/aaron/catkin_ws/src/mycobot/data/CameraCalibration.xml', cv2.FileStorage_READ)
    # Asssigning variables from xml file
    LcameraMatrix = cv_file.getNode('LcameraMatrix').mat()
    LnewCameraMatrix = cv_file.getNode('LnewCameraMatrix').mat()
    distL = cv_file.getNode('LdistCoeffs').mat()
 
    #Capture the video from webcam
    capL = cv2.VideoCapture(1)

    #Gets the camera parameters and prints it to terminal
    print("Frame incoming resolution: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    capL.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capL.set(cv2.CAP_PROP_FRAME_HEIGHT, 1980)
    print("Frame resolution set to: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    
    #Error checking
    if(capL.isOpened() == False):
        print("Error opening the video file")
    else:
        os.system("v4l2-ctl --device /dev/video1 -c focus_auto=0") 
        os.system("v4l2-ctl --device /dev/video1 -c focus_absolute=0")

    while capL.isOpened():
        
        #Read the incoming images
        success1,Limg = capL.read()
        #Rotate the images
        # Limg = (cv2.rotate(Limg,cv2.ROTATE_90_COUNTERCLOCKWISE))
        h,w = Limg.shape[:2]
        # Undistort with Remapping
        mapxL, mapyL = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
        Ludst = cv2.remap(Limg, mapxL, mapyL, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT,0)
        # Acitivate Aruco/Charuco Function Normal mode and TextOnlyMode and records markercount
        Limg= DetectPose(Ludst,draw=True)
    
        
        #Window name location and size parameters
        cv2.namedWindow("LeftCamPose",cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("LeftCamPose", 800, 800)

        # Display the Image
        cv2.imshow("LeftCamPose",Limg)
        
        keys = cv2.waitKey(1) & 0xFF
        
        #Wait ms between frames and if q is pressed break the while loop
        if keys == ord('q'):
            break
        elif keys == ord('r'):
            plt.close('all') 
            Go = True
        
    # Release webcam feeds and close all windows   
    capL.release()
    cv2.destroyAllWindows()       
    

if __name__ == "__main__":
    main()


