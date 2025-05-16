
# 인코딩 하기
'''
a = "Life is too short"
b = a.encode("UTF-8")

print(type(b))
print(b)    # b'Life is too short'  <- bytes 로 인코딩 됨


a = "한글"
# a.encode("ascii")     <- UnicodeEncodeError 발생
print(a.encode('euc-kr'))   # b'\xc7\xd1\xb1\xdb'   바이트 코드로 encode
'''

# 디코딩 하기
'''
a = '한글'
b = a.encode('euc-kr')
# print(b.decode('utf-8))   <-- encode와 같은 방식으로 decode하여야 한다.
print(b.decode('euc-kr'))
'''

# 입출력과 인코딩
# 주의사항
# 1. 입력으로 받은 바이트 문자열 --> (되도록) 유니코드 문자열로 디코딩
# 2. 함수 or 클래스 등에서는 유니코드 문자열만 사용
# 3. 결과 전송하는 마지막 부분에서만 유니코드 --> 바이트 문자열로 인코딩하여 반환

# 예시
'''
# 1. euc-kr로 작성된 파일 읽기
with open('euc_kr.txt', encoding='euc-kr') as f:    # encoding 생략 시 'utf-8' 이 기본으로 지정된다.
    data = f.read() # 유니코드 문자열
    
# 2. unicode 문자열로 프로그램 수정
data = data + "\n" + "추가_문자열"

# 3. euc-kr로 수정된 문자열 저장
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)
'''

# 아래와 같이 코드 인코딩 방식을 파일 최상단에 기입한다. (utf-8이 기본이라면 생략해도 무관)
# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
