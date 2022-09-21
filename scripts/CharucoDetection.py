from calendar import c
import cv2
import cv2.aruco as aruco
import numpy as np
import time
global count 
count = 0
num = 1
endtime = 0

#Capture the video from webcam
capL = cv2.VideoCapture(1)
# capR = cv2.VideoCapture(3)

#Gets the camera parameters and prints it to terminal
print("Frame incoming resolution: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
capL.set(cv2.CAP_PROP_FRAME_WIDTH, 1900)
capL.set(cv2.CAP_PROP_FRAME_HEIGHT, 1900)
# capR.set(cv2.CAP_PROP_FRAME_WIDTH, 920)
# capR.set(cv2.CAP_PROP_FRAME_HEIGHT, 980)
print("Frame resolution set to: (" + str(capL.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(capL.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")


#Error checking
if(capL.isOpened() == False):
    print("Error opening the video file")
# if(capR.isOpened() == False):
    # print("Error opening the video file")
    
# #Aruco Marker detection function
def FindAruco(Img,camera,marker_size=4,total_markers =250, draw=True):                      # MakerSize 4X4 MAX MARKERID 1000 with drawing enabled
    global count    
    gray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)                                       # Convert to grayscale for detection
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')          # Creates a custermizable key in the format arruco.DICT_4X4_1000
    arucoDict = aruco.Dictionary_get(key)                                             # Fetches stated dictionary using the key
    arucoParam = aruco.DetectorParameters_create()                                    # Creates detector parameters default settings
    markercorners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam) # Detecs Markers and Saves boundingbox, IdNumber and rejected markers to variables
    

    
    # Creates a Churco board object used for detection size in meters
    def ChuracoBoard(squaresX=5, squaresY=4, squareLength=30, markerLength=22):
        # Create the board 
        Board = aruco.CharucoBoard.create(squaresX,squaresY,squareLength,markerLength,arucoDict)
        # Set resolotion and show board image
        boardimg = Board.draw(outSize=(640,480))
        cv2.imshow("Charuco",boardimg)
        # Detect the charuco board corners if there are detected arucomarkers 
        if (len(markercorners) > 0):
            retval, charucoCorners, charucoIds = aruco.interpolateCornersCharuco(markercorners,ids,gray,Board)
            # If corners are not found print
            if retval == 0:
                print("Failed to Interpolate Charucoboard")
    
            # Define text parameters
            font                   = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,450)
            fontScale              = 4
            fontColor              = (0,0,255)
            thickness              = 4
            lineType               = 3
            # Put charuco corner count on the image 
            cv2.putText(Img,str(retval), 
                bottomLeftCornerOfText, 
                font, 
                fontScale,
                fontColor,
                thickness,
                lineType)
            
            # If camera parameter is 'draw' draw the markers else text only^^
            if (camera == "draw"):    
                # Draws required observation of aruco markers and charuco corners if draw set to true
                if draw: 
                    aruco.drawDetectedMarkers(Img,markercorners,ids,borderColor =(0, 255,0))             #Colour BGR
                    aruco.drawDetectedCornersCharuco(Img,charucoCorners,charucoIds,cornerColor = (255,0,0))    
            
            
        # Else if no aruco markers are found
        else:
            # Then CharucocornerCount is equal to zero
            retval = 0
            print("Cannot Find Any Aurco Markers")
            
    
        # Return marker conrners count to outer function
        return retval
    
    
    # Run Charuco board function and obtain result
    cornerCount = ChuracoBoard()
    # Return charuco corners to while loop
    return cornerCount
     
    
      


#While the camera is open capLture video frames and send them to FindArucoFunction
while capL.isOpened():
    #Timmer used for saving images
    startime = time.time() 
    #Read the incoming images
    success1,Limg = capL.read()
    #Rotate the images
    # Limg = (cv2.rotate(Limg,cv2.ROTATE_90_COUNTERCLOCKWISE))
    #Convert to numpy array 
    Limg2 = np.array(Limg)
    # Acitivate Aruco/Charuco Function Normal mode and TextOnlyMode and records markercount
    markercountL = FindAruco(Limg,'draw')
    FindAruco(Limg2,'text')
    #Window name location and size parameters
    cv2.namedWindow("LeftCam",cv2.WINDOW_NORMAL)
    cv2.namedWindow("LeftCharuco",cv2.WINDOW_NORMAL)
    
    cv2.resizeWindow("LeftCam", 900, 900)
    cv2.resizeWindow("LeftCharuco", 900, 900)
    
    cv2.imshow("LeftCam", Limg2)
    cv2.imshow("LeftCharuco", Limg)
   

    #Wait ms between frames and if q is pressed break the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #Wait ms between frames and if s is pressed save image to specified folder or savees by it self every 1 second
    elif (cv2.waitKey(1) & 0xFF == ord('s')) or (startime-endtime >= 0.5):
        # If markers were detected than save
        if markercountL > 0 :
            #Save the images withot markers to folders
            cv2.imwrite('/home/aaron/catkin_ws/src/mycobot/Images/LeftImages/LImage_'+str(num)+'.png',Limg2)
            print('[INFO] {} Images saved'.format(num))
            #Increment num to avoid create differenent image names
            num += 1 
            #Updates the endtime to continue time monitoring
            endtime  = startime
   
     
# Release webcam feeds and close all windows   
capL.release()
cv2.destroyAllWindows()       