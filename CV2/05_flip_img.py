import cv2

#Flipping Images:
"""
Flipping an image involves flipping it horizontally, vertically, or both. 
Here's how you can flip an image using OpenCV:
"""
image = cv2.imread("dhoni4.jpg")

cv2.imshow("Original image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


#code to flip the image
"""
We use the cv2.flip() function to flip the image.
 This function takes two arguments: 
 the image to be flipped and a flip code that specifies the direction of the flip.
The flip code can be
    1 for horizontal flip,
    0 for vertical flip,
    or -1 for both horizontal and vertical flip.
We create three versions of the image:
horizontally flipped (horizontal_flip), vertically flipped (vertical_flip),
and both horizontally and vertically flipped (both_flip).
We display the flipped images using cv2.imshow().
"""

#flip the image horizontally
horizontal_flip = cv2.flip(image,1)

#flip the image vertically
vertival_flip = cv2.flip(image,0)

#Flip the image both horizontally and vertivally
both_flip = cv2.flip(image,-1)

#Displaying horizontally flipped image
cv2.imshow("Horizontal filp",horizontal_flip)

#displaying vertically flipped image
cv2.imshow("Vertical Flip",vertival_flip)

#Displaying both the horizontal and vertical flips at a time
cv2.imshow("Both flips", both_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()