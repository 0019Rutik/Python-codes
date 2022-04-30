import string
dict={}
data = ""
file = open("my_file.txt","w")

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] =string.ascii_letters[i-1]
print(dict)
with open("ip2_file.txt") as f:
    while(True):
        c =f.read(1)
        if not c:
            print("End of file")       
            break
        if c in dict:            
            data =dict[c]
            print(data)
        else:
            data=c
            print(data)
        file.write(data)
        print(data)
file.close()
#print(len(string.ascii_letters))

