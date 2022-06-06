# camera.py


import PIL.Image
import cv2
from PIL import Image
import imagehash

class VideoCamera1(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()

    def get_frame(self):
        hh="reg.txt"
        f=open(hh,"r")
        reg=f.read()

        register_no=reg+".txt"
        register_image = str(reg) + ".jpg"
        register_image1 = PIL.Image.open('static/photo/' + register_image)
        # f1 = open(hh1, "r")
        # reg_res = f1.read()



        success, image = self.video.read()
        frame=image

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        j = 1
        face_counts=len(faces)
        if face_counts==0:
            f = open(register_no , "w")
            f.write("" + str("Marked"))
        elif face_counts>1:
            dd=0
        else:
            side=0
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in eyes:
                i = (len(eyes))
                if i<1:
                    f = open(register_no , "w")
                    f.write("" + str("Marked"))

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                gg = "f" + str(j) + ".jpg"
                input_frame = 'faces/' + gg
                input_frame1 = PIL.Image.open(input_frame)
                hash0 = imagehash.average_hash(register_image1)
                hash1 = imagehash.average_hash(input_frame1)
                cc1 = hash0 - hash1
                if (cc1 > 25):
                    f = open(register_no , "w")
                    f.write("" + str("Marked"))
                if x<100 or x>100:
                    print(side)
                    side=side+1


            # for (x, y, w, h) in faces:
            #     mm = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #     cv2.imwrite("myface.jpg", mm)
            #     image = cv2.imread("myface.jpg")
            #     cropped = image[y:y + h, x:x + w]
            #     gg = "f" + str(j) + ".jpg"
            #     cv2.imwrite("faces/" + gg, cropped)
            #     mm2 = PIL.Image.open('faces/' + gg)
            #     rz = mm2.resize((10, 10), PIL.Image.ANTIALIAS)
            #     rz.save('faces/' + gg)
            #     j += 1

            #########################################
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
