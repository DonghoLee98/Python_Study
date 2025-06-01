import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")   # locateOnScreen() 의 .png 파일과 비교해서 box 형태(location, width, height값)로 가져옴
# print(file_menu)            # >>> Box(left=788, top=3, width=51, height=28)
# pyautogui.click(file_menu)  # 받아온 값을 그대로 click()에 넣어 사용 가능

# munje_icon = pyautogui.locateOnScreen("munje.png")
# pyautogui.click(munje_icon)   # 화면 하단에 있을 경우, 위에서부터 찾기 때문에 시간이 좀 걸림

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)   # pyautogui의 최신 버전에서는 None이 아니라 error 메시지를 출력함 -> 아래와 같이 변경

# try:
#     screen = pyautogui.locateOnScreen("screenshot.png")
# except pyautogui.ImageNotFoundException:
#     screen = None
# print(screen)

# 동일한 image가 여러 개 있을 때, 모든 image를 찾는다
# for i in pyautogui.locateAllOnScreen("python.png"):
#     print(i)


# 속도 개선
# 1. GrayScale ; 색을 흑백으로 변환 후 비교, 속도는 30% Up / 정확도는 조금 낮아짐
# munje_icon = pyautogui.locateOnScreen("munje.png", grayscale=True)
# pyautogui.moveTo(munje_icon, duration=0.25)

# 2. 범위 지정
# munje_icon = pyautogui.locateOnScreen("munje.png", grayscale=True, region=(1115, 794, 1255 - 1155, 860 - 794)) # region(x, y, width, height)
# pyautogui.moveTo(munje_icon, duration=0.25)
# pyautogui.mouseInfo() 1115, 794 / 1255, 860

# 3. 정확도 조정    python3 -m pip install opencv-python
# munje_icon = pyautogui.locateOnScreen("munje.png", confidence=0.9)  # confidence=0.9 : 픽셀의 90% 일치
# pyautogui.moveTo(munje_icon, duration=0.25)


# 자동화 대상이 바로 보여지지 않는 경우 (= 웹페이지 창 로딩시간, 파일 여는 시간 등등)
# file_menu_notepad = None

# try:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# except pyautogui.ImageNotFoundException:
#     print("못찾음...")

# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)

# 위 내용을 반복문으로 계속해서 찾고 싶을 때
import time

i = 0
while True:
    try:
        file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
        if file_menu_notepad:
            pyautogui.click(file_menu_notepad)
            break
    except pyautogui.ImageNotFoundException:
        if i >= 3:
            print("결국 찾지 못하였습니다...")
            break
        print(str(i) + "초 경과")
        pass

    i += 1
    time.sleep(1)

    # https://www.youtube.com/watch?v=exgO1LFl9x8&t=9466s
    # 3:13:38