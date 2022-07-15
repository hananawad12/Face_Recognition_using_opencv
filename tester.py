import cv2
import os
import numpy as np
import face_rec as fr
import pickle
import parser
      
#This module takes images performs face recognition
#we can test the model by using the images of TestImages  (test1->test9)
test_img=cv2.imread('TestImages/test4.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)
#print("faces_detected:",faces_detected)


#read the data and face labels
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("./trainingData.yml")
labels={}
with open("./face-labels.pickle", 'rb') as f:
	label_ids = pickle.load(f)
	labels = {v:k for k,v in label_ids.items()}

labels = {v:k for k,v in label_ids.items()}
#print(labels)
predicted_names=[]
for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    #print("confidence:",confidence)
    #print("label:",label)
    
    fr.draw_rect(test_img,face)

    name=labels[label]
    if(confidence>65):#If confidence more than 65 then don't print predicted face text on screen
        #print('unknown')
        continue

    predicted_names.append(name)
    #print(name)
    fr.put_text(test_img,name,x,y)


url='https://prav.tatarstan.ru/eng/pravit.htm'
f=parser.find_info(url,predicted_names)
if f==0:
    print("there is no any recognized images!!!!!!")

resized_img=cv2.resize(test_img,(900,700))
cv2.imshow("face detection",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows

