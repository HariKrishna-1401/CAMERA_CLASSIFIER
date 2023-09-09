import cv2 as cv

class camera:

    def __init__(self):
    #This code opens the camera
    #According to number of web cams we have give the index number in video capture
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            # If there is camera is not opened then it raises a Value error
            raise ValueError("Unable to open the camera!")
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            #ret is return value
            if ret:
                return (ret, cv.cvtColor(frame,cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None

