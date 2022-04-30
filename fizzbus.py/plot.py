# from matplotlib import pyplot as plt
# #Estimste = [1000, 1010,1786,2000,1500,100,120,150,150,170,175,18]
# plt.plot([1,2,3,4],[1,4,9,16],'g^')
# # use values 'ro' for dotted curve
# # 'r--' for red dashesh
# # 'bs'  for blue squqres
# # to show individual label values for axises we use
# # 'g^' for green triangle
# plt.ylabel("some values ")
# plt.xlabel("some values of x")
# plt.show()
from scipy import stats


Estimste = [1000, 1010,1786,2000,1500,100,120,150,150,170,175,18,26,27,81,76,65]

Estimste.sort()
m= stats.trim_mean(Estimste,0.1)
print(m)
 