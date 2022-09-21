import cv2
import apriltag
import argparse 
num = 0

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


print(width,height)


if (cap.isOpened() == False):
    print("Error opening the video file")
    


        
while cap.isOpened():
    
    sucess,Image = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(5) & 0xFF == ord('s'):
        cv2.imwrite('/home/aaron/Documents/StereoCamera/Images/Image_' + str(num) + '.png',Image)
        print('[INFO] {} Images Saved'.format(num))
        num +=1
    gray  = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)    
    # cv2.imshow('Image', gray)
   
    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    print("[INFO] {} total Apriltag detected".format(len(results)))
    # loop over the AprilTag detection results
    for r in results:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
        # draw the bounding box of the AprilTag detection
        cv2.line(Image, ptA, ptB, (0, 255, 0), 2)
        cv2.line(Image, ptB, ptC, (0, 255, 0), 2)
        cv2.line(Image, ptC, ptD, (0, 255, 0), 2)
        cv2.line(Image, ptD, ptA, (0, 255, 0), 2)
        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(r.center[0]), int(r.center[1]))
        cv2.circle(Image, (cX, cY), 5, (0, 0, 255), -1)
        # draw the tag family on the image
        tagFamily = r.tag_family.decode("utf-8")
        cv2.putText(Image, tagFamily, (ptA[0], ptA[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("[INFO] tag family: {}".format(tagFamily))
    # show the output image after AprilTag detection
    cv2.imshow("Image2", Image)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()
   
# ap =  argparse.ArgumentParser()
# ap.add_argument("-i","--image", required=True,
#     help = "path to input image containing AprilTag")
# args = vars(ap.parse_args)

# print("[INFO] Loading Images.....")
# image = cv2.imread(args["image"])
# 

# print("[INFO] Detecting AprilTags")
# options = apriltag.DetectorOptions(familees="tag36h11")
# detector = apriltag.Detector(options)
# results = detector.detect(gray)
# print("[INFO] {} total Apriltag detected".format(len(results)))
# print(results)