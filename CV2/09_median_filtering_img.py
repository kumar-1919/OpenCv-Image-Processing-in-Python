import cv2
import numpy as np

image = cv2.imread("dhoni1.jpg")

# Apply median filtering on image
median_filtered = cv2.medianBlur(image , 5)
"""
5.3.1 Median Filtering:
    Median filtering is a nonlinear filtering technique used to remove noise from an image while preserving edges.
    It replaces each pixel's value with the median value of its neighboring pixels.
    
    We use cv2.medianBlur() to apply median filtering to the image.
    The function takes the input image and the kernel size as parameters.
    A larger kernel size results in stronger noise reduction.
    We display both the original image and the median filtered image using cv2.imshow().
    """

cv2.imshow(" Original Image", image)
cv2.imshow("median filtered image", median_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()