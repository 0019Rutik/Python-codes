import numpy as np
from PIL import Image
import scipy.misc
import random
import imageio

# width = 5
# height= 4

# array = np.zeros([height, width, 3], dtype = np.uint8)
# img = Image.fromarray(array)
# img.save('test.png')
# array1 = np.zeros([100,200,3],dtype = np.uint8)
# array1[:,:100] = [225,128,0] # Orange color
# array1[:,100:] = [0,255,255]   # Blue color
# img = Image.fromarray(array1)
# img.save('test6.png')
img = imageio.imread(" ")
#img =Image.open("image.png")
count_pun = 0
count_in = 0
count = 0
#rgb_img = img.convert("RGB")

while(count <= 100000):
    x =random.randint(0,2735)
    y = random.randint(0,2480)
    z =0
    #if (r == 60):
    if (img[x][y][z] == 60):
        count_in +=1
        count +=1
    else:
        #if(r == 80):
        if(img[x][y][z] == 80):
            count_pun+=1
            count+=1
area_pun = (count_pun/count_in)*3287263
print(area_pun)