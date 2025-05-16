
# class
# 반복되는 변수 / 메서드(함수)를 미리 정해놓은 틀(설계도) 라고 생각하면 될 것임

# Python 프로그램으로 계산기를 만들어 보자

# 계산기 하나 만들기
'''
# Calculator.py
result = 0

def add(num):
    global result   # 전역변수 result를 활용한다.
    result += num   # 결괏값(result)에 입력값(num) 더하기
    return result   # 결괏값을 return 한다.

print(add(3))
print(add(4))
'''

# 계산기 두 개 만들기   :: 비효율적이다!
'''
# 한 번에 두 가지 계산을 실행하고 싶을 경우, 변수를 구분하여 값이 섞이지 않도록 한다.
result1 = 0
result2 = 0

def add1(num):      # 계산기 1
    global result1
    result1 += num
    return result1

def add2(num):      # 계산기 2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
'''

# 계산기 두 개  -->  Class 생성하여 효율적으로 만들기
'''
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):     # 덧셈 함수
        self.result += num
        return self.result

    def sub(self, num):     # 뺄셈 함수
        self.result -= num
        return self.result
    
cal1 = Calculator()     # 객체 1 번
cal2 = Calculator()     # 객체 2 번

print(cal1.add(3))
print(cal1.add(4))
print(cal2.sub(7))
print(cal2.sub(3))
'''


# class 예시    : 변수와 함수에 대한 설계도
'''
# class : 설계도
class Cookie:   # class 명은 대문자로 시작!!
    pass

# object : 객체 or 인스턴스
ChocolateCookie = Cookie()  # return 값이 나와 ChocolateCookie 변수에 인스턴스 값이 담긴다.
GingerCookie = Cookie()
'''

# Class 활용하여 계산기 만들어보기
'''
class FourCal:      # 'F'our'C'al -> 표기법... 대문자로 작성
    def __init__(self, first, second):  # 생성자 메서드 | 객체 생성 시 최초로 실행되는 메서드이다.
        self.first = first
        self.second = second
    
    def setdata(self, first, second):   # self 값은 말 그대로 자기 자신을 뜻함
        self.first = first      # self. 에 해당 값을 저장하겠다 는 것을 명시적으로 표현한다.
        self.second = second    # 파이썬에서는 반드시 이런 방식으로 메서드를 작성해 주어야 한다.

    def add(self):
        AddResult = self.first + self.second
        return AddResult
    
    def mul(self):
        MulResult = self.first * self.second
        return MulResult
    
    def sub(self):
        SubResult = self.first - self.second
        return SubResult
    
    def div(self):
        DivResult = self.first / self.second
        return DivResult
"""
a = FourCal()
a.setdata(4, 2)
# setdata 메서드의 인자는 다음과 같이 채워진다. a -> self / 4 -> first / 2 -> second
# a 안에 어떤 값을 저장하기 위해서 self가 있고, self.~~ 이런식으로 class 아래 함수에서 변수를 할당해 주는 것이다.

# 아래와 같은 방식으로 self 변수를 사용하지 않고도 메서드를 호출할 수도 있지만, 잘 사용되지 않는다.
# a = FourCal()
# FourCal.setdata(a, 4, 2)

# 아래 a.first, a.second 이런 친구들은 '객체변수' 또는 '속성' 이라고 부른다.

# 위에서 a.setdata(4, 2) 로 이미 객체변수를 저장해 두었기 때문에,
# 따로 값을 넣지 않아도 add() 메서드를 호출하게 되면 알아서 그 값을 사용하여 result 값을 반환해 준다.
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 이미 FourCal Class가 만들어져 있으니, b 객체로 다른 계산 결과를 얻을 수도 있다.
b = FourCal()
b.setdata(10, 5)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
"""
# __init__ 생성자에 (self, first, second) 로 객체 생성을 강제해 두었으므로,
# first와 second에 해당하는 인자값을 넣지 않는다면 객체 자체가 생성되지 않도록 강제할 수 있다.
c = FourCal(3, 6)   # 생성자가 있으므로, 객체 생성 시 바로 인자값을 넣어 객체를 생성한다.
print(c.add())
'''

# class 상속(inheritance)
'''
# 위에서 만든 계산기 class를 상속하는 class를 만들어 보자
# 부모 class
class FourCal:      # 'F'our'C'al -> 표기법... 대문자로 작성
    def __init__(self, first, second):  # 생성자 메서드 | 객체 생성 시 최초로 실행되는 메서드이다.
        self.first = first
        self.second = second
    
    def setdata(self, first, second):   # self 값은 말 그대로 자기 자신을 뜻함
        self.first = first      # self. 에 해당 값을 저장하겠다 는 것을 명시적으로 표현한다.
        self.second = second    # 파이썬에서는 반드시 이런 방식으로 메서드를 작성해 주어야 한다.

    def add(self):
        AddResult = self.first + self.second
        return AddResult
    
    def mul(self):
        MulResult = self.first * self.second
        return MulResult
    
    def sub(self):
        SubResult = self.first - self.second
        return SubResult
    
    def div(self):
        DivResult = self.first / self.second
        return DivResult

# 자식 class 1
# 부모 class인 FourCal에서 속성을 상속받아 MoreFourCal에서도 유효하게 사용할 수 있다.
class MoreFourCal(FourCal):
    def pow(self):  # 부모class 속성에 더하여 제곱해 주는 메서드를 하나 더 만든다.
        PowResult = self.first ** self.second
        return PowResult

# MoreFourCal class에는 pass밖에 없으나, 상속받은 속성 때문에 .add() 메서드 등 실행이 가능하다.
a = MoreFourCal(4, 2)
print(a.pow())

# 메서드 오버라이딩
# 부모 class에서 div 0 시 오류가 발생한다. 이를 개선하고자 오버라이딩 작업을 진행한다.
# 자식 class 2
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
# 자식 class에서 기존 메서드를 덮어쓸 시 자식 class의 메서드가 우선된다.

a = SafeFourCal(4, 0)
print(a.div())  # 자식 class에서 개선된 div 메서드로, 0이 return되어 출력된다.
'''

# 클래스 변수
# 클래스 내에서 공통으로 적용되는 변수
class Family:
    lastname = "Lee"

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

a.lastname = "Kim"  # a 인스턴스에 대하여 변수 값을 수정할 수도 있다.
print(a.lastname)   # a 인스턴스에 대해서만 수정이 이루어진다. (클래스 변수는 변경X)

