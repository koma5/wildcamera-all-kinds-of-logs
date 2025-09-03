import numpy as np
from PIL import Image

# Assuming 'y10_data' is a byte array containing your Y10 pixel data
width, height = 1124, 1364 # Set your image dimensions

with open('test.raw', 'rb') as file:
    # Read the raw data
    raw_data = file.read()

# Convert the raw data to a NumPy array
# Assuming the data is in Y10 format (10 bits per pixel)
# Each pixel is represented by 2 bytes (10 bits + padding)
y10_data = np.frombuffer(raw_data, dtype=np.uint16)

# Reshape the data to the correct dimensions
y10_data = y10_data.reshape((height, width))

# Convert Y10 to 8-bit grayscale
scaled_data = np.array([(pixel >> 2) for pixel in y10_data], dtype=np.uint8)
image = Image.fromarray(scaled_data.reshape((height, width)), mode='L')


# Now you can use scaled_data for further processing or visualization

# Save as PNG
image.save('output.png')

