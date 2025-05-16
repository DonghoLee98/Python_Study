
# 정규 표현식 (= 정규식)
# 복잡한 문자열을 처리할 때 사용한다.


# 예시 문제
# : 주민등록번호를 포함하고 있는 텍스트가 있다.
#   이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.

# 정규식X --> 아래와 같이 문제 해결해야 한다.
'''
# 1. 전체 text를 공백 문자로 split 한다.
# 2. 나뉜 단어가 주민번호 형식인지 검사한다.
# 3. 단어가 주민번호 형식이라면 뒷자리를 '*'로 변경한다.
# 4. 나뉜 단어를 다시 조립한다.
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        # 주민번호 자릿수가 14자리인지 | 앞의 6자리가 숫자인지 | 뒤의 7자리가 숫자인지 확인
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*"*7
        word_result.append(word)
    result.append(" ".join(word_result))

print("\n".join(result))

# .isdigit() = 문자열(str)이 '숫자'로만 이루어져 있는지 확인하는 함수
# '_'.join([a, b, c]) = 구분자 및 매개변수(list 등의 type)를 합쳐 하나의 문자열로 바꾸어 주는 함수
#                     ==> 'a_b_c'
'''

# 정규 표현식을 사용하면, 아래와 같이 간단하게 표현할 수 있다.
import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile(r"(\d{6})[-]\d{7}")
print(pat.sub(r"\g<1>-*******", data))
# 문자열 앞에 r 을 붙여, raw string이라는 것을 표시하면 SyntaxWarning이 출력되는 것을 막을 수 있다.
# Raw String : 백슬래시(\)를 Escape 문자로 인식하지 않고, 문자 그대로 처리하게 해 준다.
