import cv2

# Read an image from file
path = r"C:\Users\Saire\OneDrive\Pictures\Wallpaper\dhoni1.jpg"
image = cv2.imread(path)

# Apply bilateral filtering
bilateral_filtered_image = cv2.bilateralFilter(image, 99, 99, 10)

# Save the bilateral filtered image to your device
#cv2.imwrite('dhoni1 Wallpaper.jpg', bilateral_filtered_image)
"""
5.3.2 Bilateral Filtering:
Bilateral filtering is a nonlinear filtering technique that smooths an image while preserving edges.
It considers both the spatial distance and intensity difference between pixels when computing the weighted average.

In this code:

We use cv2.bilateralFilter() to apply bilateral filtering to the image.
The function takes the input image, the diameter of the pixel neighborhood, and the sigma values for color and space as parameters.
A larger diameter and sigma values result in stronger smoothing while preserving edges.
We display both the original image and the bilateral filtered image using cv2.imshow().
"""


# Display the original and bilateral filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Bilateral Filtered Image', bilateral_filtered_image)

#cv2.imwrite("Bilateral.jpg",bilateral_filtered_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
