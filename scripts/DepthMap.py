from curses import window
from email.mime import base
from re import L
from tkinter import BASELINE
from turtle import right
import numpy as np 
import cv2 
from matplotlib import pyplot as plt


    
# Opends camera calibration parameters
cv_file = cv2.FileStorage()
cv_file.open('CameraCalibration.xml', cv2.FileStorage_READ)
# Asssigning variables from xml file
LcameraMatrix = cv_file.getNode('LcameraMatrix').mat()
LnewCameraMatrix = cv_file.getNode('LnewCameraMatrix').mat()
RcameraMatrix = cv_file.getNode('RcameraMatrix').mat()
RnewCameraMatrix = cv_file.getNode('RnewCameraMatrix').mat()
distL = cv_file.getNode('LdistCoeffs').mat()
distR = cv_file.getNode('RdistCoeffs').mat()
Q = cv_file.getNode("QMatrix").mat()

# Opening camera map parameters to undistort and rectify images
cv_file.open('stereoMap.xml', cv2.FileStorage_READ)
# Reading and defining map variables from xml file
stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()

    
# left_image = cv2.imread('Images/StereoImages/SLImage_0.png',cv2.IMREAD_GRAYSCALE)
# right_image = cv2.imread('Images/StereoImages/SRImage_0.png',cv2.IMREAD_GRAYSCALE)





# cv2.imshow("LEFT", left_image)
# cv2.imshow("RIGHT", right_image)

# stereo = cv2.StereoBM_create(numDisparities=32, blockSize=5)
# depth = stereo.compute(left_image,right_image)
# depth1 = cv2.normalize(depth, None, alpha = 0, beta = 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F,)
# depth1 = cv2.cvtColor(depth1,cv2.CV_8UC1)
# depth = depth.astype(np.uint8)
# #depth = cv2.applyColorMap(depth, cv2.COLORMAP_JET)

# cv2.imshow("DepthMap", depth)

# if cv2.waitKey(0) == ord('q'):
#     cv2.destroyAllWindows

# plt.imshow(depth)
# plt.axis('off')
# plt.show()

#Capture video from webcam
cap_left = cv2.VideoCapture(3)
cap_right = cv2.VideoCapture(1)
cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 820)
cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 880)
cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 820)
cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 880)

while cap_left.isOpened() and cap_left.isOpened():
        
    success1,imgl = cap_left.read()
    success2,imgr = cap_right.read()
    imgl= (cv2.rotate(imgl,cv2.ROTATE_90_COUNTERCLOCKWISE))
    imgr = (cv2.rotate(imgr,cv2.ROTATE_90_COUNTERCLOCKWISE))
    # Finds the image size and puts it in the correct format
    image_size = imgl.shape[1::-1]
    w,h= image_size
    mapxl, mapyl = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)
    mapxr, mapyr = cv2.initUndistortRectifyMap(LcameraMatrix, distL, None, LnewCameraMatrix, (w,h), 5)

    # Undistort with saved maps xml file
    Ldst = cv2.remap(imgl, mapxl, mapyl, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    Rdst = cv2.remap(imgr, mapxr, mapyr, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
 
    # Convert Undistorted frames to gray then parse into stereo compution
    Ldstgray = cv2.cvtColor(Ldst, cv2.COLOR_BGR2GRAY)
    Rdstgray = cv2.cvtColor(Rdst, cv2.COLOR_BGR2GRAY)
    window_size = 16
    min_disp = 2
    num_disp = 120-min_disp
    stereo = cv2.StereoSGBM_create(minDisparity=min_disp,numDisparities=num_disp, blockSize=window_size, uniquenessRatio=10,
                                   speckleWindowSize =100,speckleRange = 32,disp12MaxDiff = 5,P1=8*3*window_size**2,P2=32*3*window_size**2)
    
    
    
    
    # depth = stereo.compute(Rdstgray,Ldstgray)
    # # Formating the depth file for cv2 display
    # depth = cv2.normalize(depth,None, alpha = 255, beta = 0, norm_type=cv2.NORM_MINMAX, dtype=1)
    # depth = ((depth.astype(np.float32)/ 16)-min_disp)/num_disp # Calculation allowing us to have 0 for the most distant object able to dete
    # depth = depth.astype(np.uint8)
    # depth = cv2.applyColorMap(depth, cv2.COLORMAP_TURBO)
    
    
    # Window setting 
    # cv2.namedWindow("OriginalLeft",cv2.WINDOW_NORMAL)
    # cv2.namedWindow("OriginalRight",cv2.WINDOW_NORMAL)
    # cv2.namedWindow("DepthMap",cv2.WINDOW_NORMAL)
    cv2.namedWindow("ALL",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Disparity",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Closing",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Color Depth",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Filtered Color Depth",cv2.WINDOW_NORMAL)
    
    
    # cv2.resizeWindow("OriginalLeft", 900, 900)
    # cv2.resizeWindow("OriginalRight", 900, 900)
    # cv2.resizeWindow("DepthMap", 900, 900)
    cv2.resizeWindow("ALL", 900, 900)
    cv2.resizeWindow("Disparity", 900, 900)
    cv2.resizeWindow("Closing", 900, 900)
    cv2.resizeWindow("Color Depth", 900, 900)
    cv2.resizeWindow("Filtered Color Depth", 900, 900)
    
    # # Show the frames
    # cv2.imshow("OriginalLeft", Ldst)
    # cv2.imshow("OriginalRight", Rdst) 
    # cv2.imshow("DepthMap",depth)
    # cv2.imshow("ALL",np.hstack((Ldst, Rdst, depth)))
    
    #########################################################################################
    # Used for the filtered image
    stereoR=cv2.ximgproc.createRightMatcher(stereo) # Create another stereo for right this time

    # WLS FILTER Parameters
    lmbda = 18000
    sigma = 10.8
    visual_multiplier = 1.0
    
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=stereo)
    wls_filter.setLambda(lmbda)
    wls_filter.setSigmaColor(sigma)
    
    # Compute the 2 images for the Depth_image
    depthL = stereo.compute(Rdstgray,Ldstgray)
    depthR = stereoR.compute(Ldstgray,Rdstgray)
    depthL = np.int16(depthL)
    depthR = np.int16(depthR)
    
    # Using the WLS filter
    filteredImg= wls_filter.filter(depthL,Rdstgray,disparity_map_right= depthR)
    filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX);
    filteredImg = np.uint8(filteredImg)
    cv2.imshow('Disparity Map', filteredImg)
    depthL= ((depthL.astype(np.float32)/ 16)-min_disp)/num_disp # Calculation allowing us to have 0 for the most distant object able to dete
    
    # Filtering the Results with a closing filter
    kernel= np.ones((3,3),np.uint8)
    closing= cv2.morphologyEx(depthL,cv2.MORPH_CLOSE, kernel) # Apply an morphological filter for closing little "black" holes in the picture(Remove noise) 

    # Colors map
    dispc= (closing-closing.min())*255
    dispC= dispc.astype(np.uint8)                                   # Convert the type of the matrix from float32 to uint8, this way you can show the results with the function cv2.imshow()
    disp_Color= cv2.applyColorMap(dispC,cv2.COLORMAP_OCEAN)         # Change the Color of the Picture into an Ocean Color_Map
    filt_Color= cv2.applyColorMap(filteredImg,cv2.COLORMAP_OCEAN) 

    # Show the result for the Depth_image
    cv2.imshow('Disparity', depthL)
    cv2.imshow('Closing',closing)
    cv2.imshow('Color Depth',disp_Color)
    cv2.imshow('Filtered Color Depth',filt_Color)
    
    # Gets corindates from left button click and estimates distance
    def coords_mouse_disp(event,x,y,flags,param):
        alpha =60
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print (x,y,depthL[y,x],filteredImg[y,x])
            average=0
            for u in range (-1,2):
                for v in range (-1,2):
                    average += depthL[y+u,x+v]
            average=average/9
            Distance= -593.97*average**(3) + 1506.8*average**(2) - 1373.1*average + 522.06
            Distance= np.around(Distance*0.01,decimals=2)
            print('Distance: '+ str(Distance)+' m')
            
            baseline = 0.075
            fx = 788
            D = baseline*fx/average
            print('Distance: '+ str(D)+' m')
         
            
            ThreeDImage= cv2.reprojectImageTo3D(depthL,Q)
            print("Points: {}".format(ThreeDImage[y,x]))
            
    
        
     # Mouse click
    cv2.setMouseCallback("Filtered Color Depth",coords_mouse_disp,filt_Color)
    
    #Wait 1ms between frames and if q is pressed break the while loop
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
   

    
   