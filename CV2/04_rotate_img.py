import cv2  #importing opencv-python's cv2

#Reading an image name to display
image = cv2.imread("dhoni3.jpg")

#Displaying the loaded image on GUI
cv2.imshow("original image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Angle of rotation required
angle = 45

#Height and width 
height,width=image.shape[ :2]
"""
Here's a breakdown of how it works:

.shape is an attribute of NumPy arrays (and thus, OpenCV images) 
that returns a tuple representing the shape of the array.
The shape tuple contains information about the dimensions of the array.
 For images, it typically has three elements: (height, width, channels).
height corresponds to the number of rows in the image.
width corresponds to the number of columns in the image.
channels (not used in this statement) corresponds to the number of color channels in the image 
(e.g., 3 for RGB images, 1 for grayscale images).
In the statement height, width = image.shape[:2], we're using Python's tuple unpacking feature 
to assign the first two elements of the shape tuple to the variables height and width. 
This allows us to easily access the height and width of the image separately.
"""

#cv2.getRotationMatrix2D()
"""
We use the cv2.getRotationMatrix2D() function to calculate the rotation matrix. 
    This function takes three arguments: the rotation center (cx, cy), the rotation angle in degrees, 
    and the scale factor.
We specify the rotation center as the center of the image (width/2, height/2).
We use the cv2.warpAffine() function to perform the rotation using the rotation matrix.
We display the rotated image using cv2.imshow()
"""
rotated_matrix =cv2.getRotationMatrix2D((width/2,height/2),angle,1)
rotated = cv2.warpAffine(image,rotated_matrix,(width,height))

cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()