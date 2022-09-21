import numpy as np
import glob
import cv2.aruco as aruco
import cv2
import time
from lxml import etree
import os

# Function to create CharucoBoard with specified marker values
def CharucoBoard(squaresX=5, squaresY=4, squareLength=.30, markerLength=.22,
                 marker_size=4,total_markers=250):
    
    # Creates a custermizable key in the format arruco.DICT_4X4_1000
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')   
    
    # Fetches stated dictionary using the key        
    arucoDict = aruco.Dictionary_get(key)
    
    # Creates the board object and board image
    Board = aruco.CharucoBoard.create(squaresX,squaresY,squareLength,markerLength,arucoDict)
    img = aruco.CharucoBoard.draw(Board,outSize=(640,480),marginSize =0,borderBits = 1)
    
    # Returns Board Image
    return Board

# MakerSize 4X4 MAX MARKERID 1000 with drawing enabled   
def FindCharuco(Imgl,marker_size=4,total_markers =250, draw=True):  
    
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
     
    # Runs CharucoBoard function to get Board object
    Board = CharucoBoard()
    
    # Refinng detected Markers using the created board object 
    markercornersl, idsl, rejectedl,recoveredidsl = aruco.refineDetectedMarkers(grayl,Board,markercornersl,idsl,rejectedl)
    
    # Detect CharucoCorners and saves the value detected, corners, and Ids to variables
    retvalL, charucoCornersL, charucoIdsL = aruco.interpolateCornersCharuco(markercornersl,idsl,grayl,Board)
      
    # If there is no Charuco corners detected print error message
    if retvalL <= 0:
        print("[INFO] Failed to interpolate charucoboard on leftcamera")
    # Check that the amount of markers are equal to 30 in both images and add to array
    if (retvalL == 12) :
        print("[INFO] Found {} markers in Limage to be used for calibration".format(retvalL))  
        # Appending array to include valid images left and right
        ids_L.append(charucoIdsL)
        imgpointsL.append(charucoCornersL)
        objectpointsL.append(objp)
    else:
        # Display message of rejected pair and there marker corner count
        print("[INFO] Found {} markers in Limage ignoring images".format(retvalL))
        
    # If drawing is enabled then draw dected markers and corners
    if draw:
        
    #     # Colour BGR - Draws detedcted aruco markers followed by charucocorners
        IMG = aruco.drawDetectedMarkers(Imgl,markercornersl,idsl,borderColor =(0, 255,0))             
        IMG =  aruco.drawDetectedCornersCharuco(Imgl,charucoCornersL,charucoIdsL,cornerColor = (255,0,0))
        # Show the image and display new corner count
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,350)
        fontScale              = 4
        fontColor              = (0,255,0)
        thickness              = 4
        lineType               = 3

        cv2.putText(IMG,str(retvalL), 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            thickness,
            lineType)
    cv2.imshow("DetectedL",IMG)
  
   
    # Returns length of corners_array number of sucessful images and Board object
    return len(imgpointsL),Board
     



def CameraCalibrationAruco():
    
    
    # Array used to store info from images processed  
    global corners_all
    global ids_L
    global objectpointsL
    global imgpointsL
    global objp
    global Limage
    corners_all = [] 
    ids_L = []
    objectpointsL = []
    imgpointsL = []
    image_size = None
    
    # Preparing objectpoints points in 3D space
    objp = np.zeros((4*3,3), np.float32)
    objp[:,:2] = np.mgrid[0:4,0:3].T.reshape(-1,2)
    objp = objp * .30
    
    
    # Creates an array of image paths in specefied folder sorts them so they are both paired correclty
    Leftimages = sorted(glob.glob('/home/aaron/catkin_ws/src/mycobot/Images/LeftImages/*png'))

    # Loops through left image path array 
    for Limage, in zip(Leftimages):
        
        # Read image in loop 
        imgL = cv2.imread(Limage)
        # Window name and location parameters
        cv2.namedWindow("ImageL",cv2.WINDOW_NORMAL)
        cv2.namedWindow("DetectedL",cv2.WINDOW_NORMAL)
        cv2.moveWindow("ImageL", 2500,30)
        cv2.moveWindow("DetectedL", 3500,30)
        cv2.resizeWindow("ImagesL", 900, 900)
        cv2.resizeWindow("DetectedL", 900, 900)
        # Prints image name and display image
        cv2.imshow("ImageL",imgL)
        # Finds the image size and puts it in the correct format
        image_size = imgL.shape[1::-1]
        w,h= image_size
        # Runs FindCharuco Function
        numofimagesused,Board = FindCharuco(imgL)
        # Holds images foe .1 second
        cv2.waitKey(10)
    
    # Callibrating camera and print out calibration variables
    print('[INFO] Data collected performing calibration on Lcam with {} images...'.format(numofimagesused))
    Lretval, LcameraMatrix, LdistCoeffs, Lrvecs, Ltvecs = aruco.calibrateCameraCharuco(imgpointsL,ids_L,Board,(w,h),cameraMatrix=None,distCoeffs=None)
    print("\nLRetval")
    print(Lretval)  
    print("\nLCameraMatrix")
    print(LcameraMatrix)
    print("\nLDistortionCoefficients")
    print(LdistCoeffs)
    print("\nLrvec")
    print(Lrvecs)
    print("\nLtvecs")
    print(Ltvecs)
    
    # NewcameraMatrix and rectangle of all good pixles
    LnewCameraMatrix, roi_L = cv2.getOptimalNewCameraMatrix(LcameraMatrix,LdistCoeffs,(w,h),0,(w,h))
    # LnewCameraMatrix = LcameraMatrix

    
  
    # Creates a file to save Camera Calibration Parameters
    print("Saving Camera Calibration Parameters..")
    cv2_file = cv2.FileStorage('/home/aaron/catkin_ws/src/mycobot/data/CameraCalibration.xml', cv2.FILE_STORAGE_WRITE)
    
    cv2_file.write('LcameraMatrix',LcameraMatrix)
    cv2_file.write('LnewCameraMatrix',LnewCameraMatrix)
    cv2_file.write('LdistCoeffs',LdistCoeffs)
    cv2_file.write('roi_L',roi_L)
    
    # Formulates projection error based on calibration results
    mean_errorL = 0
    for i in range(len(objectpointsL)):
        imgpoints2L, _ = cv2.projectPoints(objectpointsL[i], Lrvecs[i], Ltvecs[i], LnewCameraMatrix, LdistCoeffs)
        errorL = cv2.norm(imgpointsL[i], imgpoints2L, cv2.NORM_L2)/len(imgpoints2L)
        mean_errorL += errorL
    print( "Mean Projection Error LeftCam: {}".format(mean_errorL/len(objectpointsL)) )
    print(objectpointsL[0])
    print(imgpoints2L )
    print()
    print()
    print(imgpointsL[0])
    return Leftimages
        
        
def main():
   
    CameraCalibrationAruco()
    ##################USED TO DELETE IMAGES THAT FAILED AS CODE DOES NOT RUN WHEN NO MARKERS ARE SEEN
    # try:
    #     CameraCalibrationAruco()
        
    # except:
    #     print("{}  Failed to find Markers".format(Limage))
    #     os.remove(Limage);os.remove(Rimage)
   
  
    
    
    
    
if __name__ == '__main__':
    main()
    