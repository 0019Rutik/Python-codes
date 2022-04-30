import random
import string

chal1 = ['rahul','ajay','sam','sonu','sandeep']
chal2 = ['ram','day','sant','marry','good']

symbols  = list(string.ascii_letters)
samesymbol = random.choice(symbols)




for i in range(5):
    chal1[i] = random.choice(symbols) 
    chal2[i]=random.choice(symbols)

chal1[1]= samesymbol
chal2[2]= samesymbol

print(chal1)
print(chal2)