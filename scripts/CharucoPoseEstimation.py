from re import I
import cv2
import cv2.aruco as aruco
import numpy as np
import time





# Function to create CharucoBoard with specified marker values
def CharucoBoard(squaresX=5, squaresY=4, squareLength=30,markerLength=22,
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
def DetectPose(Imgl,Imgr,draw,marker_size=4,total_markers =250, ):  
    
    
    Ltvecpose = 0
    Lrvecpose = 0
    # Converts parsed image to grayscale
    grayl = cv2.cvtColor(Imgl,cv2.COLOR_BGR2GRAY)
    grayr = cv2.cvtColor(Imgr,cv2.COLOR_BGR2GRAY)
    
    # Creates a custermizable key in the format arruco.DICT_4X4_1000                                        
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')  
    
    # Fetches stated dictionary using the key       
    arucoDict = aruco.Dictionary_get(key)            
    
    # Creates detector parameters - default settings                               
    arucoParam = aruco.DetectorParameters_create()       
    
    # Detecs Markers and Saves corners, IdNumber and rejected markers to variables                          
    markercornersl, idsl, rejectedl = aruco.detectMarkers(grayl, arucoDict, parameters = arucoParam) 
    markercornersr, idsr, rejectedr = aruco.detectMarkers(grayr, arucoDict, parameters = arucoParam) 
    
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
            
            print(Lrvecpose)
            # If drawing is enabled then draw dected markers and corners
            if draw:
                Imgl = cv2.drawFrameAxes(Imgl,LcameraMatrix,distL,Lrvecpose,Ltvecpose, 50.0,3) 
                print(Ltvecpose) 
                # Show the image and display new corner count
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (0,50)
                fontScale              = 1.5
                fontColor              = (0,0,255)
                thickness              = 2
                lineType               = 3
                cv2.putText(Imgl,"X,Y,Z                         |||                 Rx,Ry,Rz", 
                    bottomLeftCornerOfText,
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
                cv2.putText(Imgl,"{},{},{}               |||       {},{},{}".format(Ltvecpose[0,0],
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
                
                cv2.circle(Imgl,((960,540)),5,(0,255,0),-1)
                # cv2.circle(Imgl,(int(imgpoints[0][0][0][0]),int(imgpoints[0][0][0][1])),5,(255,0,255),-1)
                
    # If markers are detected in right camera
    # if len(markercornersr) > 0 :
    #     # Runs CharucoBoard function to get Board object
    #     Board = CharucoBoard()
    #     # Refining detected Markers using the created board object 
    #     markercornersr, idsr, rejectedr,recoveredids = aruco.refineDetectedMarkers(grayr,Board,markercornersr,idsr,rejectedr)
    #     # Detect CharucoCorners and saves the value detected, corners, and Ids to variables
    #     retvalr, charucoCornersr, charucoIdsr = aruco.interpolateCornersCharuco(markercornersr,idsr,grayr,Board)
    #     # If the charucocorner count is greater than 25        
    #     if (retvalr>=25): 
    #             # Estimate the pose of the board
    #             Rretvalpose,Rrvecpose, Rtvecpose = cv2.aruco.estimatePoseCharucoBoard(charucoCornersr,charucoIdsr,Board,RcameraMatrix, distR,None,None)
    #             Rtvecpose = np.round(Rtvecpose,2)
    #             Rrvecpose = np.round(Rrvecpose,2)
    #             # If drawing is enabled then draw dected markers and corners
    #             if draw:
    #                 Imgr = cv2.drawFrameAxes(Imgr,RcameraMatrix,distR,Rrvecpose,Rtvecpose, 50.0,3) 
    #                 print(Rtvecpose) 
    #                 # Show the image and display new corner count
    #                 font                   = cv2.FONT_HERSHEY_SIMPLEX
    #                 bottomLeftCornerOfText = (0,50)
    #                 fontScale              = 0.6
    #                 fontColor              = (0,0,255)
    #                 thickness              = 2
    #                 lineType               = 3
    #                 cv2.putText(Imgr,"X,Y,Z                         |||                 Rx,Ry,Rz", 
    #                     bottomLeftCornerOfText,
    #                     font, 
    #                     fontScale,
    #                     fontColor,
    #                     thickness,
    #                     lineType)
    #                 cv2.putText(Imgr,"{},{},{}               |||       {},{},{}".format(Rtvecpose[0,0],
    #                                                                                     Rtvecpose[1,0],
    #                                                                                     Rtvecpose[2,0],
    #                                                                                     Rrvecpose[0,0],
    #                                                                                     Rrvecpose[1,0],
    #                                                                                     Rrvecpose[2,0]), 
    #                     ((bottomLeftCornerOfText[0]), (bottomLeftCornerOfText[1]+50)), 
    #                     font, 
    #                     fontScale,
    #                     fontColor,
    #                     thickness,
    #                     lineType)
            
    # Return the images to main function for displaying
    return Imgl,Imgr,Ltvecpose,Lrvecpose

def main():  
    
    
    # Array used to store info from images processed  
    global LcameraMatrix
    global RcameraMatrix
    global LnewCameraMatrix
    global RnewCameraMatrix
    global distL
    global distR
    TIME =0
    x = 0
    tpose = 0
    rpose = 0
      
    # Opening camera map parameters to undistort and rectify images
    cv_file = cv2.FileStorage()

    # Opends camera calibration parameters
    cv_file.open('/home/aaron/catkin_ws/src/mycobot/data/CameraCalibration.xml', cv2.FileStorage_READ)
    # Asssigning variables from xml file
    LcameraMatrix = cv_file.getNode('LcameraMatrix').mat()
    LnewCameraMatrix = cv_file.getNode('LnewCameraMatrix').mat()
    distL = cv_file.getNode('LdistCoeffs').mat()
    
    print(LcameraMatrix) 
    

    #Capture the video from webcam
    capL = cv2.VideoCapture(2)
    # capR = cv2.VideoCapture(3)

    #Gets the camera parameters and prints it to terminal
    print("Frame incoming resolution: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    capL.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capL.set(cv2.CAP_PROP_FRAME_HEIGHT, 1980)
    # capR.set(cv2.CAP_PROP_FRAME_WIDTH, 920)
    # capR.set(cv2.CAP_PROP_FRAME_HEIGHT, 980)
    print("Frame resolution set to: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")


    #Error checking
    if(capL.isOpened() == False):
        print("Error opening the video file")
    # if(capR.isOpened() == False):
        print("Error opening the video file")
        



    while capL.isOpened():
        #Read the incoming images
        success1,Limg = capL.read()
        # success2,Rimg = capR.read()
        #Rotate the images
        # Limg = (cv2.rotate(Limg,cv2.ROTATE_90_COUNTERCLOCKWISE))
        # Rimg = (cv2.rotate(Rimg,cv2.ROTATE_90_COUNTERCLOCKWISE))
              
        h,w = Limg.shape[:2]

        # Rimg2 = np.array(Rimg)
        Rimg = Limg
        
        # Undistort with Remapping
        mapxL, mapyL = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
        Ludst = cv2.remap(Limg, mapxL, mapyL, cv2.INTER_LINEAR)
        
        # Acitivate Aruco/Charuco Function Normal mode and TextOnlyMode and records markercount
        Limg,Rimg,tpose,rpose = DetectPose(Ludst,Ludst,draw=True)
    
        
        #Window name location and size parameters
        cv2.namedWindow("LeftCamPose",cv2.WINDOW_NORMAL)
        # cv2.namedWindow("RightCamPose",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("LeftCamPose", 900, 900)
        # cv2.resizeWindow("RightCamPose", 900, 900)

        # Display the Image
        cv2.imshow("LeftCamPose",Limg)
        # cv2.imshow("RightCamPose",Rimg)
        
        if x == 0:
            TIME = time.time()
            x+=1

        #Wait ms between frames and if q is pressed break the while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - TIME >1 and np.size(tpose) > 1:
            print("{},{},{}||||||{},{},{}".format(tpose[0,0],
                                                tpose[1,0],
                                                tpose[2,0],
                                                rpose[0,0],
                                                rpose[1,0],
                                                rpose[2,0]))
        
            # break
            
        
    # Release webcam feeds and close all windows   
    capL.release()
    # capR.release()
    cv2.destroyAllWindows()       
    return tpose,rpose  

if __name__ == "__main__":
    main()


