import cv2

image = cv2.imread("dhoni1.jpg")


blurred_image = cv2.GaussianBlur(image,(15,15),10)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWimdows()

"""
cv2.GaussianBlur() Function:
The cv2.GaussianBlur() function is used to apply Gaussian blur to an image.
It convolves the image with a Gaussian kernel,
which is a two-dimensional matrix representing a Gaussian distribution.
"""
# blurred_image = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY = 0, borderType = cv2.BORDER_DEFAULT)
"""
Parameters:
src: Input image (single-channel or multi-channel).
ksize:
        Size of the Gaussian kernel.
        It should be a tuple specifying the width and height of the kernel.
        For example, (5, 5) indicates a 5x5 kernel.
sigmaX:
        Standard deviation of the Gaussian kernel in the X direction.
    I   f set to 0, OpenCV calculates it based on the kernel size.
sigmaY: 
        Standard deviation of the Gaussian kernel in the Y direction.
        If set to 0, it is assumed to be equal to sigmaX.
borderType:
        Optional parameter specifying the border mode.
        It determines how the border pixels of the image are handled.
        By default, it uses cv2.BORDER_DEFAULT.
"""
