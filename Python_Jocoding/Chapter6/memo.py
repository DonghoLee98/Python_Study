import sys

'''
# print(sys.argv)
# 터미널 입력 : python memo.py -a "Life is too short"
# 출력 : ['memo.py', '-a', 'Life is too short']

option = sys.argv[1]    # '-a' | argv : Argument Value
memo = sys.argv[2]      # 'Life is too short' | 메모 내용

print(option)
print(memo)
'''

option = sys.argv[1]

if option == '-a':      # 메모 추가
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
# 터미널 창에
# python memo.py -a "메모할_내용"
# 입력해주면 memo.txt에 계속 line 추가가 된다.
elif option == '-v':    # 메모 읽기
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)
# 터미널 창에
# python memo.py '-v'
# 를 해주면 memo.txt 내의 파일을 읽어 출력해 준다.

# 터미널에서 
# type memo.txt 
# 로 텍스트 파일 내용을 출력받을 수도 있다.
