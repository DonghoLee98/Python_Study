'''
# While문 (= 반복문)
# 나무 10 번 찍기 예제
treeHit = 0
while treeHit < 10:
    # treeHit = treeHit + 1     <- 바로 아래 코드와 같이 간단하게 표현할 수 있다.
    treeHit += 1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무를 %d번 씩이나 찍었습니다" % treeHit)
    else:
        pass



# while문 (예제 1)
# 복습 : 큰따옴표 세 개로 감싸면 줄바꿈, 들여쓰기 등등 모두 상관없이 한 줄에 넣을 수 있다.
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter a Number : 
"""

number = 0
while number < 4:
    print(prompt)
    number = int(input())
    if number == 4:
        print("Quit")


# while문 (예제 2)
# break 는 while문을 바로 탈출할 수 있도록 하는 코드이다.
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# while문 (예제 3)
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
'''

# While문 맨 처음으로 돌아가기
# continue 구문을 만나게 되면, 그대로 아래 코드는 skip하고 while문 처음으로 되돌아간다.
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
print("프로그램 종료")

# 무한반복문 탈출
# Ctrl + C 눌러 강제로 Interruption을 걸어 탈출한다.
# while True:
    # print("Ctrl + C 를 눌러야 While문을 빠져나갈 수 있습니다.")




