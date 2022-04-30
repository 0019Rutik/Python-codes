import statistics
from lotlib import pyplot as plt
Estimate =[1000,1010,1786,2000,1500,100,1220,150,150,170]
y =[]

Estimate.sort()
#tv =int(0.1 * (len(Estimate)))
#Estimate=Estimate[tv:]
#Estimate = Estimate[:len(Estimate)-tv]
for i in range(len(Estimate)):
    y.append(5)
plt.plot(Estimate , y,'r--')
plt.plot([statistics.mean(Estimate)],5,'ro')
plt.plot([statistics.median(Estimate)],5,'bs')
plt.plot([375],[5],'g^')

plt.show()