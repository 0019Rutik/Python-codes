import numpy as np
from PIL import Image

# g  = np.array([[1,2,3,4] , [4,5,6,7]])
# print(g)
# print(type(g))
# print(g.shape)

# a = np.zeros((2,2))


# b = np.ones((2,2))

# c = np.full((2,2),9)
# print(a)

# print(c)

# a  = np.random.random((2,2))
# print(a)

# a  = np.array([True,False])
# print(a.dtype)

# x = np.array([[1,2],[3,4]],  dtype = np.float64)

# y = np.array([[5,6],[7,8]],  dtype = np.float64)

# #print(np.add(x,y))
# #print(x - y)
# #print(np.subtract(x,y))
# #print(x*y)
# #print( x / y)
# print(np.sqrt(x))
# print(np.sqrt(y))

# x  = np.array([[1,2],[3,4]])

# print(x.T)
# Transposse of mamtrix

# x = np.array([[1,2],[3,4]])
# print(x)
# print(np.sum(x,axis=0))
# print(np.sum(x,axis=1))


im = Image.open('image.jpeg')

pixelMap = (im.load())
# I = np.asanyarray(Image.open('image.jpeg'))
# print(I)

img = Image.new(im.mode , im.size)

pixelNew = img.load()

I = np.asarray(Image.open('image.jpeg'))
print(I)
""" 
To convertt 8bit image in 3 bit immage we have 
n^8 / n^3 = n^5

Here , 2 ^ 8 = 32
so 0-31 = 0 
32 - 63 = 1
64 - 127 = 2
128 - 159= 3
160 - 191 = 4
1922-223-224-225 ::5:6:7
"""
for i in range(img.size[0]):
    for j in range(img.size[1]):
         # print(im.size)
     #print(pixelMap[i,j])
     #     if(img.size == img.size):
     #          break
                     
     if (pixelMap[i,j] >= 0 and pixelMap[i,j] <= 31):
              pixelNew[i,j] = 0
     elif (pixelMap[i,j] >= 32 and pixelMap[i,j] <=63):
              pixelNew[i,j] = 1
     elif (pixelMap[i,j] >= 64 and pixelMap[i,j] <=95):
              pixelNew[i,j]= 2
     elif (pixelMap[i,j] >= 96 and pixelMap[i,j] <= 127):
              pixelNew[i,j] = 3
     elif (pixelMap[i,j] >= 128 and pixelMap[i,j] <=169):
              pixelNew[i,j] = 4
     elif (pixelMap[i,j] >=170 and pixelMap[i,j]<= 197):
              pixelNew[i,j] = 5
     elif (pixelMap[i,j] >=198 and pixelMap[i,j] <= 223):
              pixelNew[i,j] = 6
     elif (pixelMap[i,j] >=224 and pixelMap[i,j] <= 225):
              pixelNew[i,j]= 7 
        # print(pixe;)

     else:
          print("not done")
        
img.save('lena_2.jpeg')

j = np.asanyarray(Image.open('lena_2.jpeg'))
