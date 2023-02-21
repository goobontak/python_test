poketmon ={"A":["지우","피카추"],"B":["웅이","롱스톤"],"C":["이슬이","고라파덕"]}
print(poketmon)
print(poketmon.get("B")) 
print(poketmon.get("B")[1])
print(poketmon.keys())
print(poketmon.values())
print(poketmon.items())
del poketmon['B']
print(poketmon)
poketmon.__reversed__
print(poketmon)
poketmon['A']+=['잠만보']
poketmon['D'] =["로켓단","냐옹"]
print(poketmon)
