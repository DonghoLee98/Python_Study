# /Users/hodong/Documents/Python/Chapter5/mod1.py
# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

# 다른 파일에서 mod1.py 를 import할 때, print 등의 구문이 있으면 그대로 실행이 되어버린다.
# 따라서 Test등의 경우로 print를 찍어볼 경우, 아래의 조건문을 달아주는 등의 조치가 필요하다.
if __name__ == "__main__":
    print(add(2, 3))

print(__name__)
# result : __main__

# 다른 프로그램에서 호출할 경우,
# result : mod1     <- 파일 명이 return된다.
