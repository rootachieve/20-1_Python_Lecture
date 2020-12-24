score =int(input("성적을 입력하시오 : "))

if (score<0) or (score >100):
    print("잘못된 성적 입니다")
elif (score >=90):
    print("A 학점 입니다")
elif (score >=80):
    print("B 학점 입니다")
elif (score >=70):
    print("C 학점 입니다")
elif (score >=60):
    print("D 학점 입니다")
else :
    print("F 학점 입니다")


