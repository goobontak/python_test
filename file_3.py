kukudan_file = open("kukudan.txt","w",encoding="utf=8")
print("2 단",file=kukudan_file)
for i in range(1,10):
    print(f"2 x {i} = {2*i}",file=kukudan_file)
kukudan_file.close()