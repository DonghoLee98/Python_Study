
'''
# List 자료형 구조
odd = [1, 3, 5, 7, 9]
print(type(odd))
print(odd)

# List 안에 List가 또 들어갈 수 있다.
a = [1, 2, 3, ['a', 'b', 'c'], 5]
# 'b'를 출력하고 싶을 경우, 아래와 같이 코드를 작성한다.
print(a[3][1])
# 역순으로 가져가고 싶다면 앞서 String에서와 같이 '-' 부호를 붙여 코드를 작성한다.
print(a[-2][-1])

# list에서 부분만 가져오고 싶을 경우 [~이상 : ~미만]
# print(a[0:2])
print(a[0::2])
'''

'''
# List 더하기(add)
# 양쪽의 자료형을 통일시켜 주어야 한다.
a = [1, 2, 3]
b = [4, 5, 6]
c = 'hi'
print(a+b)
print(str(a[2]) + c)

# List 반복하기
print(a * 3)

# List 길이 출력
print(len(a))

# List 내용물 변경
a = [1, 2, 3]
a[2] = 10
print(a)

# List 내용물 삭제(Delete)
a = [1, 2, 3, 1]
del a[1]
print(a) 

# List Slicing
a = [1, 2, 3, 4, 5]
del a[0:3]
print(a)
'''


# List에 요소 추가(Append)
a = [1, 2, 3]
a.append(4)
a.append("5")
a.append([6, 7, 8])
print(a)

# List 정렬
# 정렬시 List 요소의 자료형이 통일되지 않았다면 sort되지 않음.
#  ex) a = [1, 'a', 5, 3, 'b', 2, 'c', 4]   -> a.sort() 시 Type Error 가 출력됨
a = [1, 5, 3, 2, 4]
a.sort()
print(a)

# List 요소 Reverse
# 아래와 같이 Sorting후 Reverse할 시, 내림차순으로 정렬도 가능하다.
a = [1, 5, 3, 2, 4]
a.sort()
a.reverse()
print(a)

# List 요소가 index로 몇 번째에 위치하는지 확인
a = [1, 5, 3, 2, 4]
print(a.index(5))

# List에 요소 삽입(Insert)
a = [1, 2, 3]
a.insert(2, 9)
print(a)

# List 요소 제거(Remove)
# List 앞에서부터 찾으며, 처음 Matching된 녀석만 Remove 한다.
# .reverse() 응용 시, 뒤에서부터 지울 수도 있다.
a = [1, 2, 3, 1, 3, 4, 5]
a.remove(3)
print(a)

# List 마지막 요소를 제거함과 동시에 Return한다.
# a.pop(x)    => 여기서 x에 인덱스 값을 입력하면, 해당 인덱스의 값이 pop 된다.
a = [1, 2, 3]
print(a.pop())
print(a)

# List 내 특정 요소가 몇 개 포함되어 있는지 찾는 함수.
a = [1, 2, 3, 1, 4, 3]
print(a.count(1))

 


