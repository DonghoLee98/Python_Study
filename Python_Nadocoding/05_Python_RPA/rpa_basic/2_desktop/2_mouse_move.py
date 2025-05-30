import pyautogui

# 절대 좌표로 마우스 커서 이동
# pyautogui.moveTo(100, 200)  # 지정한 위치(가로 x, 세로 y)로 마우스 이동
# pyautogui.moveTo(100, 200, duration=0.5)    # 지정한 위치로 duration(0.5 sec) 동안 이동

# pyautogui.moveTo(100, 100, duration=0.5)
# pyautogui.moveTo(200, 200, duration=0.5)
# pyautogui.moveTo(300, 300, duration=0.5)

# 상대 좌표로 마우스 커서 이동 (현재 커서가 있는 위치를 기준)
# pyautogui.moveTo(100, 100, duration=0.5)
# print(pyautogui.position()) # Point(x, y)
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position()) # Point(x, y)
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position()) # Point(x, y)

# 아래와 같이 현재 커서 위치의 x, y 값에 접근이 가능하다
p = pyautogui.position()
print(p[0], p[1])   # x, y
print(p.x, p.y)     # x, y