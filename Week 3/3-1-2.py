money=int(input("투입한 돈: "))
value=int(input("물건 값: "))
rest=money-value;
five=rest//500
num=rest%500
one=num//100
print("거스름 돈:",rest)
print("500원 동전의 개수:",five)
print("100원 동전의 개수:",one)
         
