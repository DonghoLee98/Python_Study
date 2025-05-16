
# 3과 5의 배수를 모두 더하기
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

# -> 생각해 볼 것
#  1. 3의 배수와 5의 배수는 어떻게 찾지?
#  2. 3의 배수와 5의 배수가 겹칠 때는 어떻게 하지?

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:    # 3 '또는' 5 로 나누었을 때 나머지가 0 인 경우
        result += i
print(result)


# 아래처럼 작성하게 되면 3과 5의 공배수가 중복으로 더해지게 된다.
'''
result = 0
for i in range(1, 1000):
    if i % 3 == 0:
        result += i
    if i % 5 == 0:
        result += i
print(resutl)
'''
