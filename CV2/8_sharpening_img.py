import cv2
import numpy as np

image = cv2.imread("dhoni1.jpg")

cv2.imshow("Original Image", image)

# Apply Laplacina filter for edge enhancement
laplacian = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow("Laplacian filter", laplacian)

# Convert the resluts into uint8
sharpend_image = np.uint8(np.clip(image - 0.5*laplacian, 0 ,255))

#sharpend_image2 = np.uint8(np.clip(image - 0.9*laplacian, 0 ,255))
#sharpend_image3 = np.uint8( np.clip( image - 0.9*laplacian, 0, 255))


cv2.imshow("Sharpened Image", sharpend_image)

# Destrouy the OpenCv's GUI windows
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
5.2 Sharpening Images:
        Sharpening is a technique used to enhance edges and fine details in an image,
            making them more visually prominent.
        It involves emphasizing the high-frequency components of the image, particularly the edges.

Laplacian Filter:
    One common method for sharpening images is to use the Laplacian filter.
    The Laplacian filter highlights regions of rapid intensity change in an image,
        which typically correspond to edges.
    By subtracting the Laplacian-filtered image from the original image,
        we can enhance the edges and fine details.
"""