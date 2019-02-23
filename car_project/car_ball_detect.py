import cv2
import numpy as np
from skimage import color, data, restoration
import imutils

class Ball:
    def __init__(self, name):
        self._name = name
        # x, y image coords
        self._x = 0
        self._y = 0
        # distance to ball
        self._distance = 0
        self._radius = 0
        
    def getCoords(self):
        return (self._x, self._y)
    
    def getRadius(self):
        return self._radius
    
    def setCoords(self,x,y,radius):
        self._x = x
        self._y = y
        self._radius = radius
        
    def __repr__(self):
        return "x: {}, y: {}, radius: {}".format(self._x,self._y,self._radius)
    
    

class BallDetect:
    def __init__(self):
        # list who holds detected balls
        blueBall = Ball("blue")
        self._balls = []
        self._balls.append(blueBall)
        
    def detect(self, frame):
        mask = self.getMask("blue", frame)
        coords = self.findContours(mask)
        
        # if ball was detected
        if coords:
            spatial = coords[0]
            radius = coords[1]
            self._balls[0].setCoords(spatial[0],spatial[1],radius)
            #print("x: {}, y: {}, radius: {}".format(spatial[0],spatial[1],radius))
            print(self._balls[0])
            frame = self.drawCircle(spatial,radius,frame)
        
        
        return mask, frame
        
    def getMask(self, name, frame):
        # blur frame, convert to hsv
        blurred = cv2.GaussianBlur(frame, (11,11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # boundaries for ball detection
        if name == "blue":
            blue_lower = (90,40,6)
            blue_upper = (120,255,255)
            mask = cv2.inRange(hsv,blue_lower,blue_upper)
            mask = cv2.erode(mask,None,iterations=5)
            mask = cv2.dilate(mask,None,iterations=5)
        return mask
    
    def findContours(self, mask):
        # find contours in the mask and initialize x,y coords
        nb_contours = cv2.findContours(mask.copy(),
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
        nb_contours = imutils.grab_contours(nb_contours)
        
        # check if contours are found
        if len(nb_contours) > 0:
            # find the largest contour in image
            contour = max(nb_contours,
                          key=cv2.contourArea)
            # compute x,y coords and radius
            ((x,y), radius) = cv2.minEnclosingCircle(contour)
            
            return (x,y), radius
        else:
            return None
        
    def drawCircle(self, spatial, radius, frame):
        if radius > 10:
            cv2.circle(frame, (int(spatial[0]), int(spatial[1])), int(radius),
                       (0,255,255),
                       2)
        return frame
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
