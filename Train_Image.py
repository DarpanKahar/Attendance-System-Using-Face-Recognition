import tkinter as tk
from tkinter import Message,Text
import cv2,os
from cv2 import *
import shutil
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import *
from tkinter import *
from tkinter import ttk

import os
import cv2
import numpy as np
from PIL import Image

def TrainImages():
    recognizer=cv2.face_LBPHFaceRecognizer.create()
    path='C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImages'
    def getImageWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        Ids=[]
        for imagePath in imagePaths:
            faceImg=Image.open(imagePath).convert('L')
            faceNp=np.array(faceImg,'uint8')
            Id=int(os.path.split(imagePath) [-1].split(".")[1])
            faces.append(faceNp)
            Ids.append(Id)
            cv2.imshow("trainnig",faceNp)
            cv2.waitKey(10)
            print("Image Training")
            # self.msg2.configure(text=res)
        return Ids,faces
    Ids,faces=getImageWithID(path)
    recognizer.train(faces,np.array(Ids))
    recognizer.save('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImageLabel\\Trainner.yml')
    cv2.destroyAllWindows()

    # def getImagesAndLabels(path):
    #     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    #     faces = []
    #     Ids = []
    #     for imagePath in imagePaths:
    #         pilImage = Image.open(imagePath).convert('L')
    #         imageNp = np.array(pilImage, 'uint8')
    #         Id = int(os.path.split(imagePath)[-1].split(".")[1])
    #         faces.append(imageNp)
    #         Ids.append(Id)
    #     return faces, Ids

    # def TrainImages(self):
    #     recognizer = cv2.face_LBPHFaceRecognizer.create()
    #     harcascadePath = "/usr/local/lib/python3.6/dist-packages/cv2/data/haarcascade_frontalface_default.xml"
    #     detector = cv2.CascadeClassifier(harcascadePath)
    #     faces, Id = getImagesAndLabels("/home/ankur/PycharmProjects/StudentAttendanceSystem/TrainingImages")
    #     recognizer.train(faces, np.array(Id))
    #     recognizer.save("/home/ankur/PycharmProjects/StudentAttendanceSystem/TrainingImageLabel/Trainner.yml")
    #     print("Images Trained")