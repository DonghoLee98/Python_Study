
# 함수

'''     함수의 구조는 아래와 같다.
def 함수명(매개변수):
    수행할 문장 1
    수행할 문장 2
    ...
    return 리턴값
'''

'''
# 함수 예시
def add(a, b):      # a, b 는 매개변수(parameter, = 인자, 파라미터) : 함수에서 정의되어 사용되는 변수
    result = a + b
    return result

print(add(1, 2))    # a, b 는 인수(arguments) : 함수를 호출할 때 건네주는 변수


# 입력값이 없는 함수도 존재한다.
def say():
    result = "Hi"
    return result

print(say())


# 함수 안에 print() 가 있는 경우 & 함수에 return 값이 없는 경우
def addTwo(a, b):
    print("%d와 %d의 합은 %d 입니다." % (a, b, a + b))

a = addTwo(5, 8)    # addTwo() 함수는 return 값이 없으므로, a에 None 이 담긴다. 별개로 함수 내 print()가 실행되어, 두 값의 합은 출력이 된다.
print(a)            # a에 담긴 None을 출력한다.
'''

'''
# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)  # 각 인자에 어떤 값이 들어갈지 직접 정할 수 있으며, 순서는 상관이 없어진다.
# result = sub(7, 3) 보다 더 상세히 작성하면 위와 같다.
print(result)


# 입력값이 몇 개가 될지 모를 때, 아래와 같이 함수를 작성한다.
# def 함수_이름(*매개변수):
def add_many(*args):    # args : arguments 약어
    result = 0
    for i in args:
        result = result + i
    return result

a = add_many(1, 2)
b = add_many(1, 2, 3)
c = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a)
print(b)
print(c)


# 함수의 매개변수로 *args 하나만 사용할 수 있는 것은 아니다.
def add_mul(choice, *args):
    if choice == "add":     # 매개변수 choice에 "add"를 입력했을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력했을 때
        result = 1
        for i in args:
            result = result * i
    return result

a = add_mul("add", 1, 2, 3)
b = add_mul("mul", 2, 4, 8)
print(a)
print(b)
'''

'''
# 키워드 매개변수
# 매개변수 앞 ** 붙임
# Dictionary 형태로 출력한다.
def print_kwargs(**kwargs):
    # print(kwargs)     아래처럼 key 만 입력하여 따로따로 출력해줄 수 있다.
    print(kwargs['a'])
    print(kwargs['b'])

print_kwargs(a=1, b=2)
'''

'''
# 함수의 return값은 하나
def add_and_mul(a, b):
    return a+b, a*b

# print(add_and_mul(3, 5))
# return이 하나이기 때문에 오류가 발생할 것 같지만
# a+b, a*b 값이 튜플 형태로 함께 return된다.
# 아무튼 하나임ㅋㅋ

a, b = add_and_mul(3, 5)
print(a)
print(b)


# return 값은 하나, 그리고 return을 만나면 해당 함수는 종료가 된다.
def say_nick(nick):
    if nick == "바보":
        return  # return 값이 따로 없는 함수에서, 함수를 종료하기 위해 자주 사용된다.
    print("너의 별명은 %s 입니다." % (nick))

say_nick("abc")
say_nick("바보")    # "바보"를 입력했을 때, 함수에서 print() 구문 이전 return 되어 함수가 종료된다.
say_nick("123")


# 함수 선언 시 args 값에 default value를 미리 지정해 줄 수도 있다.
# 기본값이 지정된 변수는 args 나열 중 가장 뒤로 빼주어야 한다.
def say_myself(name, age, man=True):
    print("내 이름은 %s 입니다." % name)
    print("내 나이는 %d 살 입니다." % age)
    if man:
        print("성별은 남자입니다.")
    else:
        print("성별은 여자입니다.")

say_myself("이동호", 27)
say_myself("이동순", 25, False)
# 여기서 함수의 args는 3 개이나, man은 이미 True로 지정되어 있으므로
# 함수 호출 시 인자를 던져주지 않아도 된다.

# 매개변수는 순서를 맞춰주어야 한다!!
'''

'''
# 함수 안에서 선언한 변수의 효력 범위
# "함수 내" 변수는 해당 함수 안에서만 사용된다.
a = 1               # a : 전역 변수
def vartest(a):
    a = a + 1       # a : 지역 변수 <- 함수 종료 시 없어진다.

vartest(a)
print(a)    # def vartest(a): 선언 이전 초기화된 a = 1 이 출력된다.

""" 비슷한 예시
def vartest(a):
    a = a + 1   # 여기서의 a 는 함수 안에서만 사용되고, 함수가 terminate 될 때 함께 사라진다.
vartest(3)
print(a)        # 함수 밖의 print(a), 전역 변수로 지정된 a 값이 없으므로 NameError가 발생한다.
"""
'''

'''
# 함수 안에서, 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)  # a = 1 일 때, 함수 내에서 1이 더해져 값이 return된 것을 전역변수 a로 다시 받는다.
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a    # "전역변수 a" 를 가져오는 역할을 한다.
    a = a + 1   # 윗줄에서 가져온 전역변수에, 1을 더하여 저장한다.
                # 이는 전역변수를 수정하게 되는 것이다.

vartest()
print(a)

# 번외. Mutable 자료형
b = [1, 2, 3]
def vartest2(b):
    b = b.append(4)
    # 등호 앞의 b는 지역변수이다. -> 함수가 종료되면 함께 사라지는 값이다.
    # 등호 뒤의 변수는 인자로 받은, 전역변수 값이다.
    # b.append(4) 에서 append 하는 행위 자체로, 전역변수 b의 값이 변하였기 때문에
    # 아래 print(b)에서 리스트 뒤에 4가 append되어 있는 것을 확인할 수 있다.

vartest2(b)
print(b)
'''


# Lambda 예약어
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수_이용_표현식
add = lambda a, b: a + b
result = add(3, 4)  # lambda 표현식은 return이 없어도 표현식의 결과 값을 return한다.
print(result)

# 함수의 이름을 굳이 정하지 않고, 기능만 작성할 때 활용
# 통째로 List 등에 담고 꺼내서 활용할 수 있다.
lambdalist = [lambda a, b : a + b, lambda a, b : a * b]

firstVal = lambdalist[0](3, 4)
secondVal = lambdalist[1](5, 6)
print(firstVal)     # 3 + 4 = 7
print(secondVal)    # 5 * 6 = 30





