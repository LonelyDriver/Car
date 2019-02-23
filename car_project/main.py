import time
import cv2
import numpy as np
from car_camera import Camera
from car_ball_detect import BallDetect

if __name__ == "__main__":
    camera = Camera()
    detectedBalls = BallDetect()
    while True:
        # Get the next frame.
        frame = camera.getFrame()
        mask, img = detectedBalls.detect(frame)
        # Show video stream
        cv2.imshow('orig', img)
        cv2.imshow('mask', mask)
        key = cv2.waitKey(1) & 0xFF
     
        # if the `q` key was pressed, break from the loop.
        if key == ord("q"):
            break
        
     
    # Cleanup before exit.
    cv2.destroyAllWindows()
    camera.stopStream()