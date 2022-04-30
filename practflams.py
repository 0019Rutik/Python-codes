


import string





def remove_matching_letters(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if (l1[i] == l2[j]):
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1+['*']+l2
                return [l,True]
  
  
   
    l = l1+['*']+l2
    return [l,False]





p1 = input("Inpput first number :")
p1 = p1.lower()
p1  = p1.replace(" "," ")


p2 = input("Inpput first number :")
p2 = p2.lower()
p2  = p2.replace(" "," ")

l1 = list(p1)
l2 = list(p2)

flag = True
while flag:
    ret_list = remove_matching_letters(l1,l2)
    con_list = ret_list[0]
    flag =ret_list[1]
    star_idx = con_list.index('*')
    l1 = con_list[:star_idx]
    l2 = con_list[star_idx+1:]

count = len(l1)+ len(l2)
result = ['friends','love','affection','Marriage','Enemy','sibling']

while len(result) > 1:
    split_idx = (count % len(result)) - 1
    if split_idx >=0:
        right = result[split_idx+1:]
        left  = result[:split_idx]
        result = right + left
    else:
        result = result[:len(result) - 1]   
print(result[0])