import pyautogui

# https://www.youtube.com/watch?v=exgO1LFl9x8&t=9466s

# pyautogui.sleep(3)  # 3초 대기
# print(pyautogui.position())

# pyautogui.click(1192, 91, duration=1) # x 1192, y 91 좌표를 duration 동안 이동한 뒤 마우스로 클릭
# pyautogui.click(~~~)은 아래 코드의 조합이다
# >> Drag & Drop과 같은 경우에 활용할 수 있다
# pyautogui.mouseDown() # 마우스 클릭 & Hold
# pyautogui.mouseUp()   # 마우스 클릭 떼기

# 아래 두 코드는 같은 동작을 한다
# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # clicks= 값을 조절하여 클릭 수를 변경할 수 있다

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()       # 마우스 클릭 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()         # 마우스 클릭 뗀 상태

pyautogui.sleep(3)
# pyautogui.rightClick()    # 우클릭
# pyautogui.middleClick()   # 휠클릭

# print(pyautogui.position())
# pyautogui.moveTo(1279, 230)
# MacOS 에서는 drag 등을 사용할 때 button= 값을 무조건 명시해 주어야 한다
# pyautogui.drag(100, 0, duration=0.25, button="left")    # 너무 빠른 동작으로 drag 수행이 되지 않는다면, duration= 을 추가해 준다

pyautogui.scroll(300)   # (+) 위 방향 / (-) 아래 방향으로 300만큼 scroll

