import time
from imutils.video import VideoStream
 
class Camera:
    def __init__(self):
        self.PiCamera = True
        self.frameSize = (640,480)
        # Initialize mutithreading the video stream.
        try:
            self.vs = VideoStream(src=0,
                                 usePiCamera=self.PiCamera,
                                 resolution=self.frameSize,
                                 framerate=32)
            # start camera
            self.vs.start()
            # Allow the camera to warm up.
            time.sleep(2.0)
        except ExceptionError as e:
            print(e)
 
    def getFrame(self):
        # get frame
        frame = self.vs.read()
        # if using webcame continue frame size
        if not self.PiCamera:
            frame = imutils.resize(frame,
                                   width=self.frameSize)
        return frame
            
    def stopStream(self):
        self.vs.stop()




