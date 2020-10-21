#!/usr/bin/env python3
import cv2
import os
import numpy as np
from time import sleep

cap = cv2.VideoCapture(2)

# Divide the image that the camera acquires into N_SPLITS equal horizontal sectors.
# N_SPLITS will be an environment variable we pass to the container
N_SPLITS = int(os.environ['N_SPLITS'])

#Define Color beforehand
color_label= ['Black', 'White', 'Red','Blue',
             'Yellow',
              'Green','Magenta','Cyan',]
#              'Gray',   
  #            'Purple']

color_space = np.array([[0,0,0],
                        [255,255,255],
                        [255,0,0],
                        [0,0,255],
                        [255,255,0],
                        [0,255,0],
                        [255,0,255],
                        [0,255,255]
   #                     [128,128,128],
       #                 [128,0,128]
                        ])

while(True):
    # Capture frame-by-frame
    # cap.read() read the video by frame
    # return ret and frame:
        # ret is bool type, get true if read successful, otherwise false
        # frame: 3D matrix,  the everyframe you read
    ret, frame = cap.read()

    #Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here

    if ret:
        # get dimension
        height, width, channel = frame.shape

        # split the image horizontally
        split_ary = np.linspace(0, height, N_SPLITS + 1).round()

        color_list = []
        for idx in range(len(split_ary) - 1):
            cur_R = frame[int(split_ary[idx]):int(split_ary[idx+1]), :, 0].mean()
            cur_G = frame[int(split_ary[idx]):int(split_ary[idx+1]), :, 1].mean()
            cur_B = frame[int(split_ary[idx]):int(split_ary[idx+1]), :, 2].mean()
            cur_color = np.array([cur_R, cur_G, cur_B])

            res = np.linalg.norm(color_space - cur_color, ord=2, axis=1)
            color_idx = np.argmin(res)
            color_list.append(color_label[color_idx])

        print("Color detected for current frame:",color_list)

    else:
        print("No color detected!")
    sleep(1)
