kuku={"2단":["2 X 1 = 2","2 X 2 = 4","2 X 3 = 6"]}
print(kuku)
ar = []
for x in range(3):
    ar.append(kuku.get("2단")[x])

print(type(ar[0]))
x = str(ar[0]).split(" ")
print(type(ar))

print(x[-1])