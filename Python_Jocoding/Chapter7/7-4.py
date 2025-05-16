
# 파이썬 타입 어노테이션
# 어노테이션 기능 : 변수와 함수에 Type을 지정할 수 있는 기능이다. (Python 3.5 이상)

# 동적 언어 vs 정적 언어
'''
# Python은 기본적으로 동적 언어이다.
a = 1
print(type(a))  # int
a = "1"
print(type(a))  # str
# --> 프로그램 실행 중 '변수의 Type을 동적으로 바꿀' 수 있다.
'''

# 자바의 경우, 정적 프로그래밍 언어이다.
"""
int a = 1;  // a 변수를 int형으로 지정
a = "1"     // a 변수에 문자열을 대입할 수 없다. => Compile Error
"""

# 동적 언어는 금융권, 큰 프로젝트 등 변수의 Type에 예민한 곳에서는 잘 사용하지 않으려고 한다.
# 아래와 같이 어노테이션으로 Type을 지정할 수 있다.
num: int = 1
# num = "1"

def add(a: int, b: int) -> int:     # a, b 인자는 int 값으로 받으며 return 값 또한 int(-> int:)라고 표기하였다.
    return a + b

print(add(1, 2))    
# print(add('1', '2'))  # Type이 달라도 오류는 발생하지 않는다.
# --> 어노테이션은 단지 Hint의 기능을 할 뿐이다.


# mypy를 설치하여 Type을 강제로 준수하게 할 수도 있다.
# pip install mypy
# --> 터미널 창에서 mypy 활용하여 실행 시 어노테이션으로 작성한 변수/함수의 type이 다르다는 error를 띄울 수 있다.
# python -m mypy .\Chapter7\7-4.py  또는    mypy .\Chapter7\7-4.py
