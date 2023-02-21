
# with - 파일 open / close 대체

with open("sports.txt","w",encoding="utf-8") as sports_file:
    sports_file.write("좋아하는 운동은 농구 입니다.")
    sports_file.write("\n싫어하는 운동은 천국의계단 입니다.")
    print("\n자주하는 운동은 숨쉬기 운동입니다.",file=sports_file)
    