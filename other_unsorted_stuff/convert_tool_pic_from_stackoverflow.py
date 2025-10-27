#!/usr/bin/env python3

import numpy as np
import cv2 as cv

# Define width and height, open file and reshape
w, h = 640, 480
d = np.fromfile('KocH-file.raw', dtype=np.uint16).reshape((h,w))

# Red is every second row, every second column, starting from 0
R = d[0::2,0::2]
# Green is every second row, every second column, starting from 1
G = d[1::2,1::2]
# Synthesize Blue channel as being equal to Green
B = G

# Stack channels to make BGR image amd save
BGR = np.dstack((B,G,R))
cv.imwrite('result.png', BGR<<6)
