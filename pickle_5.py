import pickle

kuku_file = open("kukudan_2.txt","rb")
kuku = pickle.load(kuku_file)
kuku_file.close()

for x in range(2,10):
    print(f"     {x}단      ",end="")
print()
for x in range(1,10):
    print(kuku[str(x)+"단"])
print("")

'''
for x in range(2,10):
    print(kuku(x))
    
    '''