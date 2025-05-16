
# 모듈
# 모듈을 직접 제작할 일은 크게 없으므로, 사용자 관점에서 배워보자
# class와는 조금 다른 개념... 그냥 import 하여 해당 파일의 코드를 가져다 사용하겠다는 의미

# '인터프리터'에서 사용하기 위해서는 mod1.py 저장한 디렉터리로 이동하여야 읽어들일 수 있음에 주의하자.
# /Users/hodong/Documents/Python/Chapter5/mod1.py

# mod1
'''
import mod1
print(mod1.add(3, 4))

from mod1 import add, sub   # mod1 중 add라는 함수만 가져오겠다는 의미
print(add(3, 5))            # mod1 을 명시하지 않아도 활용이 가능하다.
print(sub(6, 2))            # import에서 add만 가져온다면 sub 함수는 활용이 불가능하다.
'''

# mod2
'''
import mod2
# print(mod2.PI)

a = mod2.Math()     # a 라는 객체에 mod2의 class를 할당한다.
print(a.solv(2))    # class 아래 solv라는 메서드를 인자를 던져주며 호출한다.
'''

# mod3  <-- 5-2.py와 동일한 폴더에 있지 않을 때
# import sys    --> 절대경로를 넣어주어야 한다.
import sys
print(sys.path) # 파이썬 라이브러리가 설치되어 있는 디렉토리 목록을 보여준다.

# 패키지 설치 시,, 웬만해서는 경로를 알아서 추가하기 때문에 지적 허영심 정도로만 생각.


