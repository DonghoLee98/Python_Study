
# Boolean 자료형
# 주로 if문 안에서 사용된다.
# True / False  -> string이랑은 다르다.
# 무조건 첫 글자는 대문자 이다.
a = 1 == 1
b = 1 == 2
print(a)
print(b)

# 자료형마다 참 / 거짓이 정해져 있다.
# String, List, Tuple 등의 경우 안에 값이 있다면 True, 없다면 False로 처리한다.
# 0이면 False, 이 외 숫자면 True이다.

# 참/거짓 확인하려면 아래와 같이 코드를 작성한다.
a = bool([])
b = bool([1, 2, 3])
print(a)
print(b)

