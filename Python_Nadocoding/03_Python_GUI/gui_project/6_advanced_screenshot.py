import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") # ex) _20250519_104036
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))   # ex) image_20250519_104036.png

keyboard.add_hotkey("F9", screenshot)   # User가 F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("a", screenshot)  # User가 'a' 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("Ctrl+shift+s", screenshot)   # 여러 키 조합도 가능!

keyboard.wait("esc")    # User가 "ESC" 키를 누르면 프로그램 종료