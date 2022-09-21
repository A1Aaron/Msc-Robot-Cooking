import cv2
import cv2.aruco as aruco
import numpy as np
import time

def main():
    
    # Variable for imagename file
    num = 0
    
    # Camera parameters to undistort and rectify images
    cv_file = cv2.FileStorage()
    cv_file.open('stereoMap.xml', cv2.FileStorage_READ)

    stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
    stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
    stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
    stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()
    
    #Capture video from webcam
    cap = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(3)

    #Gets the camera parameters and prints it to terminal
    print("Frame default resolution: (" + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    print("Frame resolution set to: (" + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")")

    while cap.isOpened():
     
        
        success1,img1 = cap.read()
        success2,img2 = cap2.read()
        img1 = (cv2.rotate(img1,cv2.ROTATE_90_COUNTERCLOCKWISE))
        img2 = (cv2.rotate(img2,cv2.ROTATE_90_COUNTERCLOCKWISE))
        # Undistort with remaping differnt map values
        Ldst = cv2.remap(img1, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
        Rdst = cv2.remap(img2, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
        # Show the frames
        cv2.imshow("OriginalLeft", img1)
        cv2.imshow("OriginalRight", img2) 
        cv2.imshow("StereoCalibratedLeft", Ldst)
        cv2.imshow("StereoCalibratedRight", Rdst) 
        
        
        #Wait 1ms between frames and if q is pressed break the while loop
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        #Wait 1ms between frames and if s is pressed save image to specified folder
        if cv2.waitKey(5) & 0xFF == ord('s'):
            cv2.imwrite('/home/aaron/Documents/Robotics Project/StereoCamera/Images/StereoImages/SLImage_'+str(num)+'.png',img1)
            # cv2.imwrite('/home/aaron/Documents/Robotics Project/StereoCamera/Images/StereoImages/SRImage_'+str(num)+'.png',img2) 
            print('[INFO] {} Images saved'.format(num))
            num += 1 
        
    
        
    # Release webcam feeds and close all windows   
    cap.release()
    # cap2.release()
    cv2.destroyAllWindows()       
    
if __name__ == '__main__':
    main()
        