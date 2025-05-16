
# 정규 표현식 시작하기

# 메타 문자(Meta Characters) 를 사용한다.
# 메타 문자란? : 특별한 의미를 가진 문자
# 메타 문자 예시 : . ^ $ * + ? { } [ ] \ | ( )


# 문자 클래스 [ ]
'''
[abc]

 - [] 사이의 문자들과 매치
 - "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
 - "before" --> "b" 매치
 - "dude" --> 매치 X
 - 하이픈을 사용하여 From ~ To 표현 가능
    ex) [a-c] = [abc], [0-5] = [012345]
'''

# Dot (.)
'''
a.b

 - 줄바꿈(\n)을 제외한 모든 문자와 매치
 - "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 '.' 과 잎치하므로 정규식과 매치
 - "a0b" --> "0"와 '.' 매치
 - "abc" --> "a" 문자와 "b" 문자 사이에 어떤 문자라도 하나 있어야 하므로, 매치 X
'''

# 반복 (*)  0회 반복 인정
'''
ca*t

 - "ct"는 "a"가 0번 반복되어 매치
 - "cat"는 "a"가 1번 반복되어 매치      (1번 반복)
 - "caaat"는 "a"가 3번 반복되어 매치    (3번 반복)
'''

# 반복 (+)  최소 1회 이상 반복
'''
ca+t

 - "ct"는 "a"가 0번 반복되어 매치 X     (최소 1회 반복 필요)
 - "cat"는 "a"가 1번 반복되어 매치      (1번 반복)
 - "caaat"는 "a"가 3번 반복되어 매치    (3번 반복)
'''

# 반복 ({m,n}, ?)
'''
ca{2}t      : 반복 횟수를 지정

 - "cat"는 "a"가 1 번만 반복되어 매치 X
 - "caat"는 "a"가 2 번 반복되어 매치        (2번 반복)
 
ca{2, 5}t   : 반복 범위를 지정

 - "cat"는 "a"가 1 번만 반복되어 매치 X
 - "caat"는 "a"가 2 번 반복되어 매치        (2번 반복)
 - "caaaaat"는 "a"가 5 번 반복되어 매치     (5번 반복)

ab?c        : {0, 1}, 다시 말해 없거나 있어도(1 개) 된다

 - "abc"는 "b"가 1 번 사용되어 매치
 - "ac"는 "b"가 0 번 사용되어 매치
'''


# re모듈    <- 파이썬에서 정규 표현식을 지원하는 표준 라이브러리 이다.
'''
# re : regular expression
import re
p = re.compile('[a-z]+')   # '패턴 객체' 를 생성한다.

# 패턴 객체에는 아래 4 가지 메서드를 사용할 수 있다.
# match(), search(), findall(), finditer()
'''

# match()   : 문자열의 처음부터 정규식과 Matching되는지 조사한다.
'''
import re
p = re.compile('[a-z]+')
# m = p.match("Python 3")   --> Match되지 않으므로 None이 출력된다.
m = p.match("python")
print(m)
# -->   <re.Match object; span=(0, 6), match='python'>  이런 식으로 match 객체가 출력된다.
'''

# search()  : Match와 같이 정규식과의 Matching 결과를 출력하나, 문자열 중간에서부터 match 되는지까지 모두 검사한다.
'''
import re
p = re.compile('[a-z]+')
m = p.search("12 python 3")
print(m)
# --> <re.Match object; span=(3, 9), match='python'>    문자열의 3 ~ 9 번째 요소가 match된다는 것을 확인할 수 있다.
'''

# findall()
import re
p = re.compile('[a-z]+')
m = p.findall("Life is too short")
print(m)
# --> Match하는 것들을 모두 list로 반환해 준다. ['ife', 'is', 'too', 'short']

