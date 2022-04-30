# from PIL import Image
# from numpy import transpose
# #Opeming the image 
# img = Image.open('pythonfile/obtained.jpeg')

# # Transposing 
# transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# # save it to human understandable format

# transpose_img.save('corrected.jpeg')
# print('Done fliping')
# Image enhancement 



import cv2

#c Read the image CLAHE

img = cv2.imread('obtained.jpeg')

# prepre for CLAHE

clahe = cv2.createCLAHE()

# convrt to gery scale image

grey_img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

# Apply enhancement
enh_img = clahe.apply(grey_img)

#save it to file 
cv2.imwrite('enhance2.png', enh_img)


print("Done Enhancing..")


