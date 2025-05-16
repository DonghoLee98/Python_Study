
# For문
# list나 tuple 등에서 안에 들어있는 변수를 차례로 뽑아와서 활용할 때
# 예제
'''
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

test_tuple = [(1,2), (3,4), (5,6), (7,8)]
for (first, last) in test_tuple:
    print(first + last)
'''

'''
# 실생활 예제
# 1번부터 순서대로 marks 에 점수 입력
# 60점 이상인 학생은 합격이며, 학생 번호와 함께 합/불 여부를 출력한다.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


# Range 함수
# 1에서 100까지, [1, 2, ... , 100] 을 작성하고 싶을 때
# range(1, 101) 로 간단하게 표현할 수 있다.
    # a = range(1, 11)
    # print(a)
    # print(type(a))
add = 0
for i in range(1, 11):
    add = add + i
print(add)


# for와 range 활용한 구구단
# 마지막 줄 print(" ") 의 역할은 줄넘김이다.
    # print() 함수는 기본적으로 줄넘김 ("\n")을 포함하고 있다.
# print(~~, end=" ") 여기서 end=" " 는 print하고 난 뒤에 어떤 것울 추가로 write할지 정하는 코드이다.
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print("")
'''

# 리스트 컴프리헨션

# a = [1,2,3,4]
# result = []
# for num in a:
    # result.append(num*3)

# 위의 세 줄의 코드를 아래 한 줄로 축소시킬 수 있다.
# a = [1,2,3,4]
# result = [num*3 for num in a]

# 여기서 조건을 추가해 보자
a = [1, 2, 3, 4, 5, 6]
result = [num * 3 for num in a if num % 2 == 0]

# 위의 result 를 풀어서 작성하면 아래와 같다.
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)

print(result)







