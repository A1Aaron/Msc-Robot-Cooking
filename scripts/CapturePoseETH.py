import rospy
from std_msgs.msg import Float64MultiArray
import numpy as np
import cv2
import cv2.aruco as aruco
import time
posearray = []
Tposearray = []
Rposearray = []
init_time = 0
# Function to create CharucoBoard with specified marker values
def CharucoBoard(squaresX=5, squaresY=4, squareLength=30, markerLength=22,
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
def DetectPose(Imgl,marker_size=4,total_markers =250 ):  
    
    Ltvecpose = 0
    Lrvecpose = 0
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
        
        if (retvall>=10): 
            # Estimate the pose of the board
            Lretvalpose,Lrvecpose, Ltvecpose = cv2.aruco.estimatePoseCharucoBoard(charucoCornersl,charucoIdsl,Board,LcameraMatrix, distL,None,None)
            Ltvecpose = np.round(Ltvecpose,2)
            Lrvecpose = np.round(Lrvecpose,2)
            rvec = tvec = np.array([[0],[0],[0]],np.float64)
            imgpoints = cv2.projectPoints(np.array([[int(Ltvecpose[0,0])],[int(Ltvecpose[1,0])],[int(Ltvecpose[2,0])]],dtype=np.float64),rvec,tvec,LcameraMatrix,distL)
            # imgpoints = cv2.projectPoints(np.array([[int(Ltvecpose[0,0])],[int(Ltvecpose[1,0])],[int(Ltvecpose[2,0])]],np.float64),np.array([[int(Lrvecpose[0,0])],[int(Lrvecpose[1,0])],[int(Lrvecpose[2,0])]],np.float64),np.array([[int(Ltvecpose[0,0])],[int(Ltvecpose[1,0])],[int(Ltvecpose[2,0])]],np.float64),LcameraMatrix,distL)
            
            
            # If drawing is enabled then draw dected markers and corners
        
            Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Lrvecpose,Ltvecpose, 50.0,3) 
            
            # Show the image and display new corner count
            font                   = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (0,20)
            fontScale              = 0.6
            fontColor              = (0,0,255)
            thickness              = 2
            lineType               = 3
            cv2.putText(Imgl,"X|Y|Z             |||           Rx|Ry|Rz", 
                bottomLeftCornerOfText,
                font, 
                fontScale,
                fontColor,
                thickness,
                lineType)
            cv2.putText(Imgl,"{}|{}|{}    |||  {}|{}|{}".format(Ltvecpose[0,0],
                                                                Ltvecpose[1,0],
                                                                Ltvecpose[2,0],
                                                                Lrvecpose[0,0],
                                                                Lrvecpose[1,0],
                                                                Lrvecpose[2,0]), 
                ((bottomLeftCornerOfText[0]), (bottomLeftCornerOfText[1]+50)), 
                font, 
                fontScale,
                fontColor,
                thickness,
                lineType)
            
            # cv2.circle(Imgl,(int(Ltvecpose[0,0]),int(Ltvecpose[1,0])),5,(255,0,0),-1)
            # cv2.circle(Imgl,((240,320)),5,(255,0,0),-1)
            # cv2.circle(Imgl,(int(imgpoints[0][0][0][0]),int(imgpoints[0][0][0][1])),5,(255,0,0),-1)
                
    return Imgl, Ltvecpose, Lrvecpose





    
    
    
def main():  
    
    
    # Array used to store info from images processed  
    global LcameraMatrix
    global RcameraMatrix
    global LnewCameraMatrix
    global RnewCameraMatrix
    global distL
    global distR
    
    # Opening camera map parameters to undistort and rectify images
    cv_file = cv2.FileStorage()
    cv_file.open('stereoMap.xml', cv2.FileStorage_READ)
    
    # Reading and defining map variables from xml file
    stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
    stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
    stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
    stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()

    # Opends camera calibration parameters
    cv_file.open('CameraCalibration.xml', cv2.FileStorage_READ)
    # Asssigning variables from xml file
    LcameraMatrix = cv_file.getNode('LcameraMatrix').mat()
    LnewCameraMatrix = cv_file.getNode('LnewCameraMatrix').mat()
    RcameraMatrix = cv_file.getNode('RcameraMatrix').mat()
    RnewCameraMatrix = cv_file.getNode('RnewCameraMatrix').mat()
    distL = cv_file.getNode('LdistCoeffs').mat()
    distR = cv_file.getNode('RdistCoeffs').mat()
    
    
    rospy.loginfo("[INFO] Starting the CapturePoseETH node")
    rospy.init_node('CapturePoseETH',anonymous=True)

    #Capture the video from webcam
    capL = cv2.VideoCapture(1)
    #Gets the camera parameters and prints it to terminal
    print("Frame incoming resolution: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    # capL.set(cv2.CAP_PROP_FRAME_WIDTH, 920)
    # capL.set(cv2.CAP_PROP_FRAME_HEIGHT, 980)
    print("Frame resolution set to: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")


    #Error checking
    if(capL.isOpened() == False):
        print("Error opening the video file")
    


    while capL.isOpened():    

        def callback(pose):
            
            global posearray
            global init_time
            #Read the incoming images
            success1,Limg = capL.read()
            #Rotate the images
            Limg = (cv2.rotate(Limg,cv2.ROTATE_90_COUNTERCLOCKWISE))
           
            h,w = Limg.shape[:2]
          
            # Undistort with Remapping
            mapxL, mapyL = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
            Ludst = cv2.remap(Limg, mapxL, mapyL, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT,0)
            
            # Window name location and size parameters
            cv2.namedWindow("LeftCamPose",cv2.WINDOW_NORMAL)
            cv2.resizeWindow("LeftCamPose", 900, 900)
            
            # # Acitivate Aruco/Charuco Function 
            Limg, Tpose, Rpose= DetectPose(Ludst)

            pose = pose.data
            if np.size(Tpose)>1:
                poselist = (pose[0],pose[1],pose[2],pose[3],pose[4],pose[5],pose[6])
                Tposelist = ([[Tpose[0][0]],[Tpose[1][0]],[Tpose[2][0]]])  
                Rposelist = ([[Rpose[0][0]],[Rpose[1][0]],[Rpose[2][0]]])  
            else:
                Tposelist = 0
        
            
                
            ## Used for auto capture
            if np.size(Tposelist) > 1 and time.time()-init_time >2:
                posearray.append(poselist)
                Tposearray.append(Tposelist)
                Rposearray.append(Rposelist)
            
                font = cv2.FONT_HERSHEY_SIMPLEX
                Text = (0,320)
                fontScale = 0.6
                fontColor = (0,255,0)
                thickness = 2
                lineType = 3
                cv2.putText(Limg,"Arrays Appended!",Text,font,fontScale,fontColor,thickness,lineType)
                cv2.imshow("LeftCamPose",Limg)
                init_time = time.time()
                
                
                
            keys = cv2.waitKey(1) & 0xFF
            
            if keys== ord('q'):
                
                rospy.loginfo("Saving RobotPose Array: {}".format(posearray))
                np.save('posearray',posearray)
                rospy.loginfo("Saving TPose Array: {}".format(Tposearray))
                rospy.loginfo("Saving RPose Array: {}".format(Rposearray))
                np.save('charucoposeT',Tposearray)
                np.save('charucoposeR',Rposearray)
                rospy.signal_shutdown("close called")
                capL.release()
                cv2.destroyAllWindows()  
                rospy.signal_shutdown("close called")
                
            
            elif keys == ord('d'):
                
                if np.size(poselist) and np.size(Tposelist) > 0:
                    posearray.append(poselist)
                    Tposearray.append(Tposelist)
                    Rposearray.append(Rposelist)
                
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    Text = (0,320)
                    fontScale = 0.6
                    fontColor = (0,255,0)
                    thickness = 2
                    lineType = 3
                    cv2.putText(Limg,"Arrays Appended!",Text,font,fontScale,fontColor,thickness,lineType)
                    cv2.imshow("LeftCamPose",Limg)
        
            
        
                
        
            # Display the Image
            cv2.imshow("LeftCamPose",Limg)

            
    
    
        # Subscribes to topic called joint_state published by rviz
        rospy.Subscriber("/pickPointframe",Float64MultiArray,callback)
        # Keeps python code from exiting until the node is stopped
        rospy.spin()
    
   
    
       
       
    
          
    
if __name__ == '__main__':
   main()
    
    
    
    