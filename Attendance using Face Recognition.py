import cv2
import numpy as np
import face_recognition
import os
from datetime import  datetime
path = 'ImageSamples'
pathImages = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)
myImages = os.listdir(pathImages)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)

    classNames.append(os.path.splitext(cl)[0])
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

    # print(myDataList)
    print(nameList.index(name))
    i = nameList.index(name)

    data = f'{nameList[i]},PRESENT,\n'
    myDataList[i] = data
    print(data)
    f = open('Attendance.csv', 'w+')
    f.writelines(myDataList)

    print(myDataList)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (0, 0), None, 1, 1)
        # print('Done')
        encode = face_recognition.face_encodings(img)[0]
        print(len(encode))
        encodeList.append(encode)
    return  encodeList

def recongonizeImage(image):


    img = face_recognition.load_image_file(f'{pathImages}/{image}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img)
    encodeFaces = face_recognition.face_encodings(img)
    i = 0
    for enFace, faceLoc in zip(encodeFaces, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, enFace)
        faceDis = face_recognition.face_distance(encodeListKnown, enFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print('Detecting Faces ....')
            markAttendance(name)
        else:
            print('unknown')

encodeListKnown = findEncodings(images)
# print(encodeListKnown)
print('Encoding Completed ... ')
for image in myImages:
    recongonizeImage(image)