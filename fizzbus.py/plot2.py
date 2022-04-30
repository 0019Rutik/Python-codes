from matplotlib import pyplot as plt
Estimates = [1000, 1010,1786,2000,1500,100,120,150,150,170,175,18]

#x_values =[1,2,3,4]
#y_values = [5,4,6,2]

#plt.plot(x_values,y_values)
#plt.scatter(x_values,y_values)
y=[]
for i in range(len(Estimates)):
    y.append(5) 
Estimates.sort()
tv = int(0.1*(len(Estimates)))
Estimates=Estimates[:len(Estimates)-tv]

plt.plot(Estimates,5,'r--')                             
             
plt.show()