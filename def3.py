def football(name,team,*positon):
    print(f"이름 : {name}\n소속팀 : {team}\n",end='역활 : ')
    for i in positon:
        print(i,end=',')
print()
    
football("리강인","마요르카","공격수,미드필더,센터","수비수","골키퍼","슈퍼루키")