import cv2

image = cv2.imread("dhoni2.jpg")
cv2.imshow("Original Image",image)

# 4.1  Creating RGB Image
"""
4.1 RGB Color Space:
The RGB color space represents colors as combinations of red, green, and blue components.
Each color is represented by three values ranging from 0 to 255,
indicating the intensity of each component.

We use cv2.cvtColor() to convert the image from the default BGR color space to RGB color space.
The conversion is done using the flag"""#cv2.COLOR_BGR2RGB.
"""We then display both the original BGR image and the converted RGB image using cv2.imshow().
"""
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


# Gray Scale Image
"""
4.2 Grayscale Color Space:
The grayscale color space represents images using a single channel,
where pixel values indicate the intensity or brightness of each pixel.
Grayscale images are often used for simplicity and efficiency in image processing tasks.

We use cv2.cvtColor() to convert the image from the BGR color space to grayscale.
The conversion is done using the flag""" #cv2.COLOR_BGR2GRAY.
"""We display both the original BGR image and the grayscale image using cv2.imshow().
"""
Gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# HSV Image
"""
4.3 HSV Color Space:
HSV (Hue, Saturation, Value) is a color space that represents colors based on their
hue, saturation, and value/brightness components.
It is often used for color-based segmentation and analysis tasks.
We use cv2.cvtColor() to convert the image from the BGR color space to HSV.
The conversion is done using the flag """#cv2.COLOR_BGR2HSV.
"""
We display both the original BGR image and the HSV image using cv2.imshow().
HSV is particularly useful for tasks like color segmentation, 
where colors are identified based on their hue and saturation values.
"""
hue_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# YUV Image
yuv_image = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
"""
4.4 YUV Color Space:
YUV is a color space that represents colors as combinations of luma (Y) and chrominance (U and V) components.
It is commonly used in video compression and processing applications.

We use cv2.cvtColor() to convert the image from the BGR color space to YUV.
The conversion is done using the flag """#cv2.COLOR_BGR2YUV.
"""
We display both the original BGR image and the YUV image using cv2.imshow().
YUV is particularly useful for video processing tasks,
where separating luma and chrominance components can improve compression efficiency.
"""


# Display RGB Image
cv2.imshow("RGB Image",rgb_image)
# Display Gray Image
cv2.imshow("Gray Image",Gray_image)
# Display HUE image
cv2.imshow("HUE image",hue_image)
# Display YUL Imae
cv2.imshow("YUV Image",yuv_image)

# Closing The OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()