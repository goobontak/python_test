kukudan_file= open("kukudan.txt","r",encoding="utf=8")
kukudan = kukudan_file.read()
print(kukudan)
kukudan_sp=kukudan.split("\n")
print(kukudan_sp)

for i in range(1,10):
    kuku=kukudan_sp[i].split(" ")
    print(kuku[-1])
  

kukudan_file.close()