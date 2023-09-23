import cv2 as cv
import numpy as np
#--------------------------------------------------------------------------------
# function description :
# Streaming using webcam in real life and make track bar to edit color space (HSV) using OpenCV library.
#--------------------------------------------------------------------------------
# parameters :
# typeOfMask : type of mask (AND or OR)
#--------------------------------------------------------------------------------
def editColorSpace(typeOfMask):
    def nothing(x):
        pass
    # start streaming
    cap = cv.VideoCapture('Video.mp4')
    # create 2 new windows
    cv.namedWindow('image')
    cv.namedWindow('mask')
    # create track bar for lower HSV value
    cv.createTrackbar('L-H', 'mask', 0, 255, nothing)
    cv.createTrackbar('L-S', 'mask', 0, 255, nothing)
    cv.createTrackbar('L-V', 'mask', 0, 255, nothing)
    
    while True:
        _, frame = cap.read()
        # convert frame from BGR to HSV color space
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # get track bar position
        h = cv.getTrackbarPos('L-H', 'mask')
        s = cv.getTrackbarPos('L-S', 'mask')
        v = cv.getTrackbarPos('L-V', 'mask')
        # add lower HSV value
        lower_blue = np.array([h, s, v])
        upper_blue = np.array([130, 255, 255])
        # create mask using lower and upper HSV value
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        # create result using frame and mask (AND or OR)
        if typeOfMask == 'and':
            res = cv.bitwise_and(frame, frame, mask=mask)
        elif typeOfMask == 'or':
            res = cv.bitwise_or(frame, frame, mask=mask)
        # show frame and result
        cv.imshow('image', frame)
        cv.imshow('mask', res)
        # press ESC to close the webcam 
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break

    # close the webcam
    cap.release()
    # close all windows
    cv.destroyAllWindows()

#--------------------------------------------------------------------------------
# function description :
# Streaming using webcam in real life and make track bar to edit color space (HSV) using OpenCV library using 6 track bars for lower HSV value and upper HSV value.
#--------------------------------------------------------------------------------
# parameters : None
#--------------------------------------------------------------------------------

def advancedEditColor():
    # usless function to use in trackbar :D
    def nothing(x):
        pass
    # start streaming
    cap = cv.VideoCapture(0)
    # create 2 new windows
    cv.namedWindow('image')
    cv.namedWindow('mask')
    # create track bar for lower HSV value and upper HSV value (3 track bars for each)
    cv.createTrackbar('L-H', 'mask', 0, 255, nothing)
    cv.createTrackbar('L-S', 'mask', 0, 255, nothing)
    cv.createTrackbar('L-V', 'mask', 0, 255, nothing)
    cv.createTrackbar('U-H2', 'mask', 255, 255, nothing)
    cv.createTrackbar('U-S2', 'mask', 255, 255, nothing)
    cv.createTrackbar('U-V2', 'mask', 130, 255, nothing)

    while True:
        _, frame = cap.read()
        # convert frame from BGR to HSV color space
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # get track bar position for lower HSV value and upper HSV value
        h = cv.getTrackbarPos('L-H', 'mask')
        s = cv.getTrackbarPos('L-S', 'mask')
        v = cv.getTrackbarPos('L-V', 'mask')
        h2 = cv.getTrackbarPos('U-H2', 'mask')
        s2 = cv.getTrackbarPos('U-S2', 'mask')
        v2 = cv.getTrackbarPos('U-V2', 'mask')
        # add lower HSV value and upper HSV value 
        lower_blue = np.array([h, s, v])
        upper_blue = np.array([h2, s2, v2])
        # create mask using lower and upper HSV value
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        res = cv.bitwise_and(frame, frame, mask=mask)
        # show frame and result
        cv.imshow('image', frame)
        cv.imshow('mask', res)
        # press ESC to close the webcam 
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break

    # close the webcam
    cap.release()
    # close all windows
    cv.destroyAllWindows()