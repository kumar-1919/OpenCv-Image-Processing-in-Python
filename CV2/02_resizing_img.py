import cv2

image  = cv2.imread("dhoni1.jpg")

if image is not None :
    print ("Image loaded succesfully")
else:
    print("Image loaded unsuccessfully")

cv2.imshow("image", image)
print("Image displayed successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()
#resizing the image to a new width and height
new_width = 400
new_height = 300
#resized Image is 
resized_image = cv2.resize(image, (new_width,new_height))

# Save resized Image
# cv2.imwrite(" resized_image.jpg", resized_image)

# Syntax
# cv2.imwrite(" image_name.jpg or .png or .jpeg ..." ,  variable in which image stored)

"""
We use the cv2.resize() function to resize the image.
The first argument is the image we want to resize.
The second argument is a tuple (new_width, new_height) specifying the new dimensions of the image.
The function returns the resized image.
We display the resized image using cv2.imshow()
"""

if resized_image is None :
    print("Resizing failed")
else :
    print("resizing is successfull")

#displaying resized image
cv2.imshow("resized image", resized_image)

print("Resized Image displayed successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()
