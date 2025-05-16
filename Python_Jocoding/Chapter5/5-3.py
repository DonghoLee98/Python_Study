
# 패키지    : 관련 있는 모듈의 집합, 계층적으로(디렉터리 구조) 관리할 수 있다.

# 가상의 Game 패키지 예시
"""
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
"""

# from game.sound import *
# 여기서 * 는, 모든 파일을 선택한다는 뜻이다.
# * 는 __init__ 안의 __all__ 에 명시되어 있는 파일들을 가져온다.


# 접근자
# ..    : 이전 디렉터리
# .     : 현재 디렉터리


# Alias
import mod2 as m2   # mod2 를 m2라고 칭하고, 이후 코드 작성 시 m2만 작성하여도 mod2를 호출할 수 있다.