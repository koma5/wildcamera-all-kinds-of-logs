#!/usr/bin/env python3

import numpy as np
import cv2 as cv

# Define width and height, open file and reshape
w, h = 1536, 864
# Read the raw file as uint16 and reshape
d = np.fromfile('test.raw', dtype=np.uint16).reshape((h, w))

# Extract the red and green channels from the RG10 format
# Each pixel is represented by 10 bits, so we need to shift and mask
R = (d[0::2, 0::2] >> 6) & 0x3FF  # Red channel
G = (d[1::2, 1::2] >> 6) & 0x3FF  # Green channel
# Synthesize Blue channel as being equal to Green
B = G

# Stack channels to make BGR image and save
BGR = np.dstack((G, B, R)).astype(np.uint8)  # Convert to uint8 for saving
cv.imwrite('result.png', BGR<<6)
