def evolve(x):
    if(x == 1):
        




with open("dna_data.txt") as myfile:
    x = myfile.read()
    x =list(x)
for i in range(0, 10000):
    evolve(x)
print(x)