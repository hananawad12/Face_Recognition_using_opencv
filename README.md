# Face_Recognition_using_opencv_Internship_2022
# Prerequisites:
numpy <br />
opencv-python <br />
opencv-contrib-python <br />
pickle <br />
requests <br />
# Installation:
in command line: <br />
pip install numpy <br />
pip install opencv-python <br />
pip install opencv-contrib-python <br />
pip install pickle <br />
pip install requests <br />

# Running:
1.Put some images in TestImages folder that we want to predict in tester.py <br />
2.Put the Images of training for the classifier in trainingImages folder. If we  want to train clasifier to recognize multiple people then 
 we can add the images of each person in folder and add the name of person for each folder. <br />
3. then Run  <br />
*python face_rec.py <br />
-Note if you have trainingData.yml and faceLabels.pickle then you can run tester.py directly. <br />
*python tester.py <br />

# Output
1. if there are any recognized images will show the test image with detected faces and names, print the personal information which got from official websites in cmd and  finally open the web browser with the personal information. <br />
2. if there are no any recognized images will show the test image and print there is no any recognized images!!! in cmd <br />

