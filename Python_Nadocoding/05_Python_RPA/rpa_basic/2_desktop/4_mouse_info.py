import pyautogui
# pyautogui 모듈 사용 간 마우스를 display 네 귀퉁이로 가져다 두면 알아서 종료가 된다.
# 그럴 때 강제로 진행하고 싶다면 아래 FAILSAFE 를 False 로 둔다.
# pyautogui.FAILSAFE = False

pyautogui.PAUSE = 1 # .sleep(1) 과 동일한 동작, global 적용

# 마우스 커서가 위치한 곳의 information (x, y 좌표, 색상값 등)을 확인할 수 있는 창을 띄운다
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)