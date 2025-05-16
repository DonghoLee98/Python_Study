
# 집합 자료형 : Python에서만 <set> 자료형으로 제공한다.
# 주로 List 자료형에서 중복제거 하는 곳에서 활용한다.
# List를 Set으로 변경하여 중복제거 후 다시 list(set()) 으로 List 자료형으로 변경한다.
# list(set()) 으로 처리 시, 어느정도 순서는 정렬시켜준다.
li = [1, 2, 2, 2, 3, 3, 4]
li = list(set(li))
print(li)

'''
# 아래 코드는 List를 set 형식으로 변경한다.
s1 = set([1, 2, 3])
# 또는
s1 = {1, 2, 3}
print(type(s1))
print(s1)

# string 자료형 또한 set 자료형으로 사용할 수 있다.
# "Hello"  ->  {'e', 'o', 'l', 'H'}  =>  순서가 따로 정해지지 않음에 주의
s1 = set("Hello")
print(s1)

# 집합은 중복을 허용하지 않는다.
# = 각 요소들이 모두 고유하다.
'''

# 교 / 합 / 차 집합
'''
# 교집합 -> set 자료형 2 개 사이 & (s1 & s2) // intersection 함수 사용 (s1.intersection(s2))
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 -> | 또는 .union()
print(s1 | s2)
print(s1.union(s2))

# 차집합 -> - 또는 .difference
# 차집합 시 앞 뒤 순서가 중요하다.
print(s1 - s2)
print(s2.difference(s1))
'''

# set자료형 관련 함수

# 집합 내 요소 1 개 추가 -> .add()
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 집합 내 요소 여러 개 추가 -> .update()
# 중복 요소 포함 시 중복제거
s1 = set([1, 2, 3])
s1.update([4, 4, 5, 6])
print(s1)

# 집합 내 요소 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)





