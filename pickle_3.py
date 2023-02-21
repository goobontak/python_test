import pickle
kuku_file = open("kukudan_2.txt","wb")
kukudan = {"1단":[],"2단":[],"3단":[],"4단":[],"5단":[],"6단":[],"7단":[],"8단":[],"9단":[]}
for x in range(2,10):
    for i in range(1,10):
        ku = (f"{x} X {i} = {x*i:>2}")
        kukudan[str(i)+"단"] += [ku]
        print(ku)

pickle.dump(kukudan,kuku_file)

kuku_file.close()
