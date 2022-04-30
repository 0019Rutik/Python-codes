str1 = input("Enter the String")
str2 = input("Enter the String")
count1=0
i=0
while(i < len(str1)):
    count1 = count1 + ord(str1[i])
    i =i+1
print(count1)
count2 = 0
i =0
while(i < len(str2)):
    count2 = count2 + ord(str2[i])

    i=i+1
print(count2)
if(count1 == count2):
    print("These  are Anagrams ")
else:
    print("Theese are Not anagrams")