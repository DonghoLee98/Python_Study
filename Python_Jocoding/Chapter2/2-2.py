'''
head = "PYTHON"
tail = " is Fun!"

# print(head + tail)

# head에 할당된 변수를 3 회 반복 출력할 때, 아래와 같은 방법을 사용한다.
# print(head * 3)

# 터미널 창에 '=' 등으로 구분할 때와 같은 상황에서 효과적으로 사용할 수 있다.
print("=" * 50)
print(head + tail)
print("=" * 50)
'''

'''
# 문자열 길이는 아래와 같이 구한다.
a = "Life is too short, You Need PYTHON"
print(len(a))


# 인덱싱
# 인덱스는 0 부터 시작한다.
# 0부터 시작, a의 3번 인덱스는 4번째 알파벳인 'e'가 나오게 된다.
# - 부호 사용시, 역으로 계산되어 출력된다.
print(a[0])
print(a[3])
print(a[15])
print(a[-1])
# print(a[-35])     <= index out of range 오류 발생함.


# 슬라이싱
# 아래 코드는 b = a[0] + a[1] + a[2] + a[3] 와 동일하다.
# a[0:4:1]    <= 0 이상, 4 미만, 2의 간격으로 가져온다.
# 각각 공란으로 둔다면      처음부터 : 끝까지 : 1의 간격
# - 부호 사용시, 인덱싱의 예와 유사하게 역으로 계산된다.
b = a[0:4] 
print(b)

c = '20241205Windy'
date = c[:8]
whether = c[8:]
print(date)
print(whether)
'''

'''
# 숫자 대입
# %d : Decimal 뜻으로, 정수값이 입력된다. (실수는 %f)
a = "I ate %0.3f apple(s)" % 10.123874
print(a)

# 문자열 대입
# %s : String 뜻으로, 문자열 값이 입력된다. 
a = "I ate %s apple(s)" % "Six"
print(a)

# 응용
# 변수를 미리 초기화 해준 뒤에 대입도 가능하다.
# 변수의 타입을 맞춰주는 것 중요
number = 4
day = "Three"

a = "I ate %d apple(s) for %s Days" % (number, day)
print(a)


# a = "%-10sjane." % 'hi'
a = "%10s jane." % 'hi'
print(a)

# 또 다른 포맷팅 방법
a = "I eat {0} apples".format(3)
print(a)

# {0}, {1}, ... 순서대로 format(~, ~, ~ ...) 값이 들어가게 된다.
number = 5
day = "Five"
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)
'''

'''
# 가장 최신 포맷팅
name = "이동호"
age = 27
a = f"이름은 {name}이고, 나이는 {age}이다."
# 중괄호 내에서 python 연산이 가능하다.
b = f"내년에는 {age + 1}살이 된다."
print(a)
print(b)
'''

a = "hobby"
print(a.find('y'))
print(a.index('h'))
# a.find와 a.index 차이는, 없는 값을 찾으려고 할 때 find는 -1을, index는 error를 출력한다.

 
a = ', '.join("abcd")
print(a)

# 대/소문자 바꾸기
a = "ABCD"
b = "abcd"
print(a.lower())
print(b.upper())


# 공백 지우기 (좌, 우, 양쪽)
a = " Hello "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 문자열 Replace, split
# Split 시, 결과값은 list형태로 출력된다.
a = 'Life is too short'
print(a.replace('Life', 'Leg'))
print(a.split())

b = 'a:b:c:d'
print(b.split(':'))





