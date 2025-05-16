
# 클로저 & 데코레이터


# 클로저란? 간단히 말해 함수 안의 함수 이다.
# *3, *5, *7, ... 을 return 하는 함수를 만들 때 숫자마다 만들어 주어야 한다.
# --> 효율적으로 Class 라는 것을 사용하면 쉽게 만들 수 있다.
'''
class Mul:
    def __init__(self, m):
        self.m = m
    
    def mul(self, n):
        return self.m * n
    
    def __call__(self, n):  # 위의 mul 함수를 함수명 없이 사용할 수 있다.
        return self.m * n

# Mul class를 활용하여 3, 5를 곱해주는 함수를 바로바로 만들어 쓴다.
if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)
    
    # print(mul3.mul(10))
    # print(mul5.mul(10))
    
    print(mul3(10))     # 메서드를 명기하지 않도고, 바로 __call__ 로 들어간다.
    print(mul5(10))
    
# 위에 보다 조금 더 간단하게, __call__ 을 사용할 수도 있다.
'''


# 클로저
'''
# 함수 안에 함수가 있고, 안에 있는 함수를 return해주는 것이 '클로저'이다.
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper      # wrapper 함수 자체를 return 해준다.

if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)
    
    print(mul3(10))     # return 으로 함수를 받았으므로, 기존 함수 사용하듯이 하면 된다.
    print(mul5(20))     # 이렇게 mul() 과 같은 함수를 클로저(closer)라고 한다.
'''


# 데코레이터

# 함수의 실행 시간이 궁금할 때, 다음과 같이 코드를 작성한다.
'''
import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간 : %f 초" % (end - start))

myfunc()
'''

# 시간을 확인해 보아야 할 함수가 많다면, 위의 함수를 동일하게 여러 번 만들어야 하며, 비효율적이다.
# --> 클로저를 활용, function 자체를 return 받도록 하여 중복되는 구문을 줄인다.
'''
import time

def elapsed(original_func):     # * elapsed : 경과
    def wrapper():
        start = time.time()
        result = original_func()    # 해당 line에서 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간 : %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result   # 기존 함수의 수행 결과를 return 한다.
    return wrapper

"""
def myfunc():
    print("함수가 실행됩니다.")
    
decorated_myfunc = elapsed(myfunc)  # myfunc 함수도 객체이므로, 인자로 활용할 수 있다.
decorated_myfunc()  # myfunc 를 인자로 하는 elapsed 라는 함수를 실행한다.
"""

# decorrated_myfunc 처럼 함수로 한 번 받아주지 않고도 데코레이터를 활용할 수 있는 방법이 있다.
# 함수 위에 @ + 함수명 이 있으면 데코레이터 함수로 인식한다.
@elapsed
def myfunc():
    print("함수가 실행됩니다.")
    
myfunc()
'''

# 만약 실행하는 myfunc() 함수가 인자를 필요로 한다면?
# def elapsed() 함수 안에도 인자를 추가해 주면 된다.
import time

def elapsed(original_func):
    def wrapper(*args, **kwargs):   # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs)    # 해당 line에서 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간 : %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result   # 기존 함수의 수행 결과를 return 한다.
    return wrapper

@elapsed
def myfunc(msg):
    print("'%s'를 입력합니다." % msg)
    
myfunc("You Need Python")   # 출력할 메시지를 myfunc(msg) 인자로 전달한다.  

