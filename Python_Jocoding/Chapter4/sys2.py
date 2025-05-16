import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
    
    
# import sys 사용하지 않는 방법 (일단 개념은 위의 코드와 동일하다)
def up(*args):
    for i in args:
        print(i.upper(), end=' ')
        
up = ["hello", "world", "dh"]