city1 = {6:"서울,화성",2:"경기",3:"제주"}

city = ["서울","경기","인천","제주","부산","강릉","포항"]

print(city1)
print(city)
print("""
      """)
print(city1[6])
print(city1.get(2))
print(city1.get(9,"해당없음"))

animal={'A':"Alpaca",'B':"Bear",'C':"Cat",'D':"Dog"}
print(animal.get('C'))
print(animal.get("D"))