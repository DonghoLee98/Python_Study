
'''
# 튜플 자료형
# List와 유사하나, 수정이 불가능하다.

# Mutable   : 변경 가능 (List, Dictionary, 집합 등)
# Immutable : 변경 불가능 (정수, 실수, 문자열, 튜플 등)
'''

# 튜플의 경우, 아래와 같이 소괄호를 사용한다.
# 일반적인 소괄호 사용하는 상황과 구분하기 위해 요소가 하나만 있더라도 콤마를 표시해 준다.
# List와 같이 인덱스로 표현 또한 가능하다.
t1 = (1,)
t2 = (1, 2, 3)
print(t1)
print(t2[1])
print(type(t1))

# 괄호가 없어도 tuple을 만들 수 있다
t3 = 1, 2, 3
print(t3)
print(type(t3))

# tuple 안에 tuple이 또 들어갈 수 있다.
t4 = ('a', 'b', ('c', 'd', ('e', 'fg')))
print(t4)

# 아래는 tuple을 del할 때의 예시이다.
# 역시나 오류가 발생한다.   => TypeError : 'tuple' object doesn't support item deletion
t5 = (1, 2, 'a', 'b')
# del t5[2]

# tuple Slicing 시, 기존의 tuple Data는 살아있다.
t6 = (1, 2, 'a', 'b', 'c')
print(t6[2:])
print(t6)

# tuple 덧셈이 가능하다.
# 아래 t3을 t1로 바꿔 새로운 tuple(t1)을 만들 수 있다.
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)
print(type(t3))

# tuple 곱하기, 길이 구하기 또한 가능하다.
print(t1 * 3)
print(len(t1))


