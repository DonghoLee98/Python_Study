import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # (현재 터미널에서 지정된 directory 아래로) 파일로 저장

# pyautogui.mouseInfo()
# 1045,19 34,164,241 #22A4F1

pixel = pyautogui.pixel(1045, 19)
print(pixel)

# print(pyautogui.pixelMatchesColor(1045, 19, (34,164,241)))    # True
# print(pyautogui.pixelMatchesColor(1045, 19, pixel))           # True
# print(pyautogui.pixelMatchesColor(1045, 19, (34,164,243)))    # False

