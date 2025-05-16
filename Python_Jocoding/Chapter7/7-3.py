
# 이터레이터와 제너레이터

# 이터레이터
# a = [1, 2, 3]
# for i in a:
#   print(i)
# 여기서 리스트 [1, 2, 3] 처럼 반복 구문에 사용할 수 있는 객체를
# '반복 가능(iterable) 객체' 라고 한다.

# 이터레이터란? next()를 호출하여 다음 값을 호출하는 것
'''
a = [1, 2, 3]
ia = iter(a)
print(type(ia)) # type은 'list_iterator' 이다.
print(ia)       # iter 함수의 값이 출력되지 않고 메모리 위치가 출력된다.

print(next(ia)) # next() 로 iterator의 값을 하나씩 출력할 수 있다.
print(next(ia))
print(next(ia))
print(next(ia)) # list 요소가 3 개인데 4 번째 next를 출력하려 하면 'StopIteration' error가 발생한다.
'''

# for문을 사용하여 언제 next()가 끝날지 신경쓰지 않고도 값을 출력할 수 있다.
'''
a = [1, 2, 3]
ia = iter(a)
# 1 번 for 문
for i in ia:
    print(i)
# 2 번 for 문   <-- 이미 위에서 list를 모두 출력해 버려, 다음으로 출력할 수 있는 요소가 남아있지 않아 출력이 되지 않는다.
for i in ia:
    print(i)
'''


# 이터레이터 직접 만들어보기
'''
# 이터레이터 class
class MyIterator:
    def __init__(self, data):
        self.data = data        # iteral한 값을 받는다
        self.position = 0       # 예로, list에서 해당 요소의 위치(index 값)이다.
        
    def __iter__(self):         # __iter__ 로 인해 해당 메서드는 반복 가능한 객체가 된다.
        return self
    
    def __next__(self):         # __iter__와 항상 세트로 작성되어야 한다.
        if self.position >= len(self.data): # 더 이상 반복할 객체가 없으면 StopIteration error를 raise 한다. * len() : data의 총 갯수
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result       # 반복 가능한 객체를 하나씩 return 한다.
    
if __name__ == "__main__":
    i = MyIterator([1, 2, 3, 4])
    for item in i:
        print(item)
'''

# 역 이터레이터 만들기  (iterable 객체를 역순으로 출력)
'''
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1  # [-1] 이면 배열에서 가장 뒤의 요소를 말한다.
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    
if __name__ == "__main__":
    i = ReverseIterator([1, 2, 3])
    for item in i:
        print(item)
'''


# 제너레이터란? 이터레이터를 생성해 주는 함수이다.
'''
# 예시
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
    
g = mygen()
# print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # 이터레이터와 마찬가지로, 배열의 크기를 벗어나면 'StopIteration' error가 출력된다.
'''

# 제너레이터 표현식
'''
"""
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()
"""
gen = (i * i for i in range(1, 1000))   # 이는 제너레이터 표현식이며, 대괄호로 감싸게 되면 list 표현식이다.

print(next(gen))
print(next(gen))
print(next(gen))
'''

# 제너레이터의 활용
'''
# 아래 코드를 실행하면 list_job을 뽑으면서 5회 전부 실행한 뒤 [0]을 print할 수 있다.
import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1 초 지연
    return "done"

list_job = [longtime_job() for i in range(5)]   # 해당 구문을 사용하면서 5 번 1초를 기다린다.
print(list_job[0])
'''

# [0] 하나만 실행하려면 list_job을 list 자료형이 아닌 generator로 처리한다.
# Lazy Evaluation(느긋한 계산법) 이라고 한다.
import time

def longtime_job():
    print("job start")
    time.sleep(1)   # 1 초 지연
    return "done"

list_job = (longtime_job() for i in range(5))   # 해당 구문을 사용하면서 5 번 1초를 기다린다.
print(next(list_job))   # 'job start' 가 한 번만 돌고 바로 'done'이 실행된다.
# --> list와 다르게 모든 값을 메모리에 올려두고 실행하는 것이 아닌, 그때그때 메모리에 올려서 사용한다.
