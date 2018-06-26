from tkinter import filedialog
from tkinter import *
import cv2

print("Click any key to close application.")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
root=Tk()
img=cv2.imread(filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
root.destroy()
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Gray image decreases noise

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)#adjust and minNeighbours scaleFactor accordingly for best result

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

r_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Face Detector (Click any key to close)",r_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
