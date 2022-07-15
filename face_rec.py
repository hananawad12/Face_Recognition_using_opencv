import cv2
import os
import numpy as np
import pickle

#Given an image returns rectangle for face detected
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade=cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')#Load haar classifier
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)#detectMultiScale returns rectangles

    return faces,gray_img

#Given train images return the x_train data and y_labels
def labels_for_training_data():
    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "TrainImages")
    for root,subdirnames,filenames in os.walk(image_dir):
        for file in filenames:
            if file.endswith("png") or file.endswith("jpg"):
                img_path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]

            test_img=cv2.imread(img_path) 
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img) 
            if len(faces_rect)!=1:
               continue
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]
            x_train.append(roi_gray)
            y_labels.append(id_)
    return x_train,y_labels,label_ids


#trains haar classifier which takes x_train, y_labels returned 
def train_classifier(x_train,y_labels):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(x_train,np.array(y_labels))
    return face_recognizer

#draws bounding boxes around detected face in image
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=2)

#writes name of person for detected label
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)




#Train the data and save it
x_train,y_labels,label_ids=labels_for_training_data()
face_recognizer=train_classifier(x_train,y_labels)
face_recognizer.save('trainingData.yml')

#save the labels
with open("./face-labels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)

