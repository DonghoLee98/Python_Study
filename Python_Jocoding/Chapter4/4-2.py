
# 사용자 I/O
# 사용자에게 직접 input값을 받아 프로그램을 실행한다.
'''
a = input()

print(type(a))      # 입력받은 내용은 무조건 문자열(String)로 들어온다.
print("유저가 입력한 내용 : " + a)
'''


# print()문
print("life" "is" "too short")  # 1 번
print("life"+"is"+"too short")  # 2 번
# 1 번 print문에서 자동으로 + 를 해 준다.

# 콤마(,)를 활용, String 값들을 나열해 주면 자동으로 띄워쓰기가 된다.
print("life", "is", "too short")

for i in range(1, 10):
  # print(i, end="\n")  <- end="\n"을 추가하여도 아무것도 적지 않았을 때와 동일하게 작동한다.
    print(i, end=" ")




