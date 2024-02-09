import cv2

#read an image
image = cv2.imread("dhoni4.jpg")

if image is not None:
    print("Image loaded successfully")
else :
    print("Image loading failed")

#display image 
cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#define the coordinates of the new image to be formed by cropping
x,y,width,height = 100,100,300,300

#crop the image

"""
We specify the coordinates of the region to be cropped using the variables x, y, width, and height.
We use NumPy array slicing to extract the region of interest from the original image.
We display the cropped image using cv2.imshow()
"""

crop_image = image[y:y+height,x:x+height]

if crop_image is not None:
    print("Image cropped successfully")
else :
    print("Image loading failed")

#display cropped image

cv2.imshow("New Image",crop_image)

#GUI closing time 
cv2.waitKey(0)
cv2.destroyAllWindows()