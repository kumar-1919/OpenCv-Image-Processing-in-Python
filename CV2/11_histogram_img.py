import cv2

# Read an image from file
image = cv2.imread('dhoni1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)
"""
5.3.3 Histogram Equalization:
Histogram equalization is a technique used to adjust the contrast of an image by redistributing pixel intensities.
It enhances the visibility of details in both dark and bright areas of the image.

We use cv2.equalizeHist() 
to apply histogram equalization to the grayscale image.
The function enhances the image contrast by redistributing pixel intensities based on the image histogram.
We display both the original grayscale image and the equalized image using cv2.imshow().
Histogram equalization is effective at improving image contrast and enhancing details,
especially in images with low contrast or uneven lighting conditions.

"""

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
