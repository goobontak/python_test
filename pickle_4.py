import pickle

kuku_file = open("kukudan_2.txt","rb")
kuku = pickle.load(kuku_file)
print(kuku)
kuku_file.close()
