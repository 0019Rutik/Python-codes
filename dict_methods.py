myDict ={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("options avillable are:",myDict.keys())
a = input ("enter meaning of the word\n")

print("the meaning of the word is :",myDict.get(a))

