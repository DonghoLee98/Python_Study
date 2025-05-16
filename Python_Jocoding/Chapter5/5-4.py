
# 예외처리
# error가 return될 때 처리하는 방법

# Error - 예시
# 1 : f = open("파일명_없음", 'r')  -->  FileNotFoundError 가 발생한다.
# 2 : num = 4 / 0
# 3 : a = [1, 2]
#     print(a[2])


# 예외처리 - 형태
"""
try:
    # 오류 발생 가능성이 있는 구문
except Exception as e:
    # 오류가 발생했을 때 실행
else:
    # 오류가 발생하지 않았을 때 실행
finally:
    # 무조건 마지막에 실행
"""


# 예시 1
'''
try:
    4 / 0
except ZeroDivisionError as ZeroError:
    # print(ZeroError)
    print("0으로 나누는 오류가 발생!!")
'''


# 예시 2
'''
try:
    f = open("파일명_없음", 'r')
    # ... 무언가를 수행한다.
finally:
    f.close()   # 중간에 오류가 발생하더라도 무조건 실행한다.
'''


# 여러 오류 처리
'''
try:
    a = [1, 2]
    print(a[3])     # go to IndexError
    4 / 0           # go to ZeroDivisionError
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다!")
# except IndexError:
#     print("인덱싱 할 수 없습니다!")
except (ZeroDivisionError, IndexError) as Error:    # Tuple로 묶어서도 출력이 가능하다.
    print(Error)
'''


# try - else 문
'''
try:
    age = int(input("나이를 입력해 주세요 : "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입이 금지됩니다.")
    else:
        print("환영합니다!")
'''


# 오류 회피하기기
'''
try:
    f = open("파일명_없음", 'r')
except FileNotFoundError:
    pass
'''


# 오류 일부러 발생시키기
'''
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    # pass      <-- 상속받은 fly 메서드가 에러가 발생한다. 오버라이드를 강제로 해 주어야 한다!!
    def fly(self):
        print("펄럭펄럭")

eagle = Eagle()
eagle.fly()
'''


# 나만의 Error 만들어 사용하기
class MyError(Exception):
    pass
    # def __str__(self):    <-- 추가하게 되면 아래 as e: 에서 지정된 error 메시지가 출력된다.
    #     return "허용되지 않는 nickname 입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")    # MyError class에서 e가 아직 할당되지 않아 빈칸으로 출력된다.
except MyError as e:
    print(e)
