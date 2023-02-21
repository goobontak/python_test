import pickle

kuku_file = open("kukudan_2.txt","rb")
kuku = pickle.load(kuku_file)
kuku_file.close()

for x in range(2,10):
    print(f"{x}단 : ",end="")
    print(kuku[str(x)+"단"])