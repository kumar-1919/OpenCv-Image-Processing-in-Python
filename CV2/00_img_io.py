import cv2
# Importing opencv's  cv2 module

# Loading an Image file
image = cv2.imread("dhoni1.jpg")

# Confirming whether the image loaded successfully or not
if image is not None:
    print("Image was successfully loaded!")
else:
    print("Failed to load image.")

#Displaying the loaded image using OpenCV's window    
cv2.imshow('image',image)

# Closing OpenCV's windows
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.waitKey(0):
"""
 This function waits for a keyboard event for a specified amount of time (in milliseconds). 
 In this case, 0 indicates that the function will wait indefinitely until a key is pressed. 
 It's commonly used with cv2.imshow() to display an image and wait for a key press before 
 closing the window.
"""
#cv2.destroyAllWindows(): 
"""
This function destroys all OpenCV windows that are currently open.
 It's used to clean up any OpenCV windows created during image processing.
"""
