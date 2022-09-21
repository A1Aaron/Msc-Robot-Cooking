import numpy as np
import cv2

   
   
   
   
def main():
    state = True
    num = 0
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
    roi_L = cv_file.getNode('roi_L').mat()
    roi_R = cv_file.getNode('roi_R').mat()
    ROI_L = cv_file.getNode('ROI_L').mat()
    ROI_R = cv_file.getNode('ROI_R').mat()

    # Formats the valid rectangle data to allow the use of rectangle asignment
    roi_L = np.matrix.transpose((roi_L)).astype(int)
    roi_R = np.matrix.transpose((roi_R)).astype(int)
    ROI_L = np.matrix.transpose((ROI_L)).astype(int)
    ROI_R = np.matrix.transpose((ROI_R)).astype(int)
    
    # Open both cameras
    cap_left =  cv2.VideoCapture(1)
    # cap_right = cv2.VideoCapture(1)                  
    cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 1980)
    # cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


    while(cap_left.isOpened()):

        # Read capture video frames
        succes_left, frame_left = cap_left.read()
        # succes_right, frame_right = cap_right.read()
        frame_left= (cv2.rotate(frame_left,cv2.ROTATE_90_COUNTERCLOCKWISE))
        # frame_right = (cv2.rotate(frame_right,cv2.ROTATE_90_COUNTERCLOCKWISE))
        h,w = frame_left .shape[:2]
        
        # Window setting 
        cv2.namedWindow("Frame Left1",cv2.WINDOW_NORMAL)
        cv2.namedWindow("Frame Left2",cv2.WINDOW_NORMAL)
        cv2.namedWindow("Frame Left3",cv2.WINDOW_NORMAL)
        # cv2.namedWindow("Frame Right1",cv2.WINDOW_NORMAL)
        # cv2.namedWindow("Frame Right2",cv2.WINDOW_NORMAL)
        # cv2.namedWindow("Frame Right3",cv2.WINDOW_NORMAL)
        cv2.namedWindow("Original FrameLeft",cv2.WINDOW_NORMAL)
        # cv2.namedWindow("Original FrameRight",cv2.WINDOW_NORMAL)
        
        cv2.resizeWindow("Frame Left1", 900, 900)
        cv2.resizeWindow("Frame Left2", 900, 900)
        cv2.resizeWindow("Frame Left3", 900, 900)
        # cv2.resizeWindow("Frame Right1", 900, 900)
        # cv2.resizeWindow("Frame Right2", 900, 900)
        # cv2.resizeWindow("Frame Right3", 900, 900)
        cv2.resizeWindow("Original FrameLeft", 900, 900)
        # cv2.resizeWindow("Original FrameRight", 900, 900)
        
        # Show original frames
        cv2.imshow("Original FrameLeft", frame_left)           
        # cv2.imshow("Original FrameRight", frame_right)
        
        # Loads the neccessary paremeters from CharucoCalibration script
        if state == True:
            # LcameraMatrix,LnewCameraMatrix,RcameraMatrix,RnewCameraMatrix, distL, distR, roi_L, roi_R, ROI_L, ROI_R = CharcuCameraCalibration.CameraCalibrationAruco()
            # print(roi_L);print(np.size(roi_L))
            state = False
            
        # Undistort
        Ldst = cv2.undistort(frame_left , LcameraMatrix, distL, None, LnewCameraMatrix)
        # Rdst = cv2.undistort(frame_right , RcameraMatrix, distR, None, RnewCameraMatrix) 
        
        # Draw the recrangle of valid pixels
        x, y, w, h = roi_L[0]
        
        cv2.rectangle(Ldst,(x,y),(x+w,y+h),(255,0,0),2)
        x, y, w, h = roi_R[0]
        # cv2.rectangle(Rdst,(x,y),(x+w,y+h),(255,0,0),2)
        # Show the frames
        cv2.imshow("Frame Left1", Ldst)           
        # cv2.imshow("Frame Right1", Rdst)
        
         #Wait 1ms between frames and if s is pressed save image to specified folder
        if cv2.waitKey(5) & 0xFF == ord('s'):
            cv2.imwrite('/home/aaron/Documents/Robotics Project/StereoCamera/Images/StereoImages/SLImage_'+str(num)+'.png',Ldst)
            # cv2.imwrite('/home/aaron/Documents/Robotics Project/StereoCamera/Images/StereoImages/SRImage_'+str(num)+'.png',Rdst) 
            print('[INFO] {} Images saved'.format(num))
            num += 1 
       
     
        
        # Undistort with Remapping
        mapxL, mapyL = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
        Ldst = cv2.remap(frame_left, mapxL, mapyL, cv2.INTER_LINEAR)
        # mapxR, mapyR = cv2.initUndistortRectifyMap(RcameraMatrix, distR, None, RnewCameraMatrix, (w,h), 5)
        # Rdst = cv2.remap(frame_right, mapxR, mapyR, cv2.INTER_LINEAR)
        # Draw the rectangle 
        x, y, w, h = roi_L[0]
        cv2.rectangle(Ldst,(x,y),(x+w,y+h),(255,0,0),2)
        # x, y, w, h = roi_R[0]
        # cv2.rectangle(Rdst,(x,y),(x+w,y+h),(255,0,0),2)
        # Show the frames
        cv2.imshow("Frame Left2", Ldst)           
        # cv2.imshow("Frame Right2", Rdst)
        
        # Undistort with remaping differnt map values
        Ldst = cv2.remap(frame_left, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
        # Rdst = cv2.remap(frame_right, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)///
        # Draw the recrangle of valid pixels
        x, y, w, h = ROI_L[0]
        cv2.rectangle(Ldst,(x,y),(x+w,y+h),(255,0,0),2)
        # x, y, w, h = ROI_R[0]
        # cv2.rectangle(Rdst,(x,y),(x+w,y+h),(255,0,0),2)
        # Show the frames
        cv2.imshow("Frame Left3", Ldst)
        # cv2.imshow("Frame Right3", Rdst) 
        


        # Hit "q" to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release and destroy all windows before termination
    # cap_right.release()
    cap_left.release()

    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()