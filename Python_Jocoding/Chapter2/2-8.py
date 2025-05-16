
# 변수 만드는 여러가지 방법


# b에 a의 메모리 주소 값을 복사
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

# b 만들 때 a의 값을 복사 붙여넣기
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# Copy 모듈 활용
from copy import copy
a = [1, 2, 3]
b = copy(a)


# 여러 방법들
# 아래 두 줄을 한 줄로 줄일 수 있다
# 예시는 tuple 자료형이며, list 자료형도 가능하다.
# 괄호는 뭐 맘대로 보기 쉽게 넣어도 되고 안넣어도 된다.
a = 'python'
b = 'life'
a, b = ('python', 'life')
(a, b) = 'python', 'life'
# 여러 개의 변수에 같은 값을 한 줄로 넣어줄 수도 있다
a = b = 'python'

# 변수 두 개의 값을 바꿔치기할 수도 있다
a = 3
b = 5
a, b = b, a
print(a)
print(b)


