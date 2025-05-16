
# 프로그래밍 시작하기

# 구구단 만들기 예시
# 가장 우선적으로 입력 및 출력을 생각한다.

'''
def gugu(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result

print(gugu(2))
'''

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result

print(gugu(3))
