import cv2

# Read an image
image = cv2.imread('dhoni1.jpg')

# Define the desired window size
desired_window_width = 800
desired_window_height = 600

# Create a named window with the desired size
cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image Window', desired_window_width, desired_window_height)

# Display the image in the window
cv2.imshow('Image Window', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
