
# 파일 생성하기

# 파일_객체 = open(파일_이름, 파일_열기_모드)

# 파일 열기 모드는 아래와 같다
# r : 읽기 모드
# w : 쓰기 모드
# a : 추가 모드 (파일의 마지막에 새로운 내용 추가시 사용)

# 파일 경로 미지정시, 해당 스크립트 저장된 위치에 파일을 생성한다.

# 아래는 "절대 경로" 를 사용하여 파일을 생성하는 코드이다. (생성할 파일의 전체 경로를 작성)
    # f = open("C:/Python/Chapter4/test.txt", 'w')
    # f.close()

'''
f = open("C:/Python/Python/Chapter4/test.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄을 출력합니다.\n" % i
    f.write(data)
f.close()
'''
# 파일 생성되었는데 열어보니 글자가 깨져있다? -> 인코딩 문제


# 파일 읽기
'''
f = open("C:/Python/Chapter4/test.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
while True:
    line = f.readline()
    if not line:        # string이 빈("") 칸이면 False 이다.
        break
    print(line)     # print(line, end="") 하면 줄바꿈 한 번만 한다.
f.close()
# 결과값이 Line 두 개를 건너뛰는데 txt파일에서 \n 한 번, print() 에서 \n 한 번
# 줄바꿈이 두 번 들어가기 때문이다.
'''

# readlines() 함수
'''
f = open("C:/Python/Chapter4/test.txt", 'r')
lines = f.readlines()   # 파일 내 line들을 List에 담아 return 한다.
for line in lines:
    line = line.strip() # line 끝의 \n 문자를 제거한다.
  # line = line.replace('\n', '')
    print(line)
f.close()

# 출력값의 줄바꿈(\n)을 제거하고 싶을 때, strip(), replace() 등의 함수를 사용한다.
'''

# read() 함수
'''
f = open("C:/Python/Chapter4/test.txt", 'r')
data = f.read()     # 파일 안의 모든 data를 통째로 읽어온다.
print(type(data))
print(data)
f.close()
'''

# 파일 객체를 for()문과 함께 사용하기
'''
# for문에 file 객체 자체를 물린다
f = open("C:/Python/Chapter4/test.txt", 'r')
for line in f:
    print(line)
f.close()
'''

# 파일에 새로운 내용 추가하기
'''
f = open("C:/Python/Chapter4/test.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄을 출력합니다.\n" % i
    f.write(data)
f.close()
'''

# with 문 사용
# 일반적인 상황에서는 file을 open()하여 작업 후 close()를 해 주어야 한다
# with문으로 자동으로 파일을 여닫을 수 있다
'''
with open("C:/Python/Chapter4/with.txt", "w") as f:
    f.write("Life is too short, you need python")   # 여기서 f는 지역변수이다!
'''

f = open("C:/Python/Chapter4/with.txt", "r")
data = f.read()
print(data)
