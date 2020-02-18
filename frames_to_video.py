import cv2
import numpy as np
import glob
import os

FRAMES_DIR = '/home/sharif/Documents/Verkehrsuebungsplatz-Auswertung/Avigilon/THC_640S_H4A_BO12/YOLACT_THC_640S_H4A_BO12_AVI_10_FPS_15'
VIDEO_F = os.path.join(FRAMES_DIR, 'video.avi') 

img_array = []
for i, f_name in enumerate(os.listdir(FRAMES_DIR)):
    if i % 50 == 0: print(i, ' / ', len(os.listdir(FRAMES_DIR)))
    file = os.path.join(FRAMES_DIR, f_name)
    img = cv2.imread(file)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter(VIDEO_F,cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    if i % 50 == 0: print(i)
    out.write(img_array[i])
out.release()