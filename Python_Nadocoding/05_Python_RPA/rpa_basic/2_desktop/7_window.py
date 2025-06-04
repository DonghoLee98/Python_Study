# MacOS -> pyautogui 지원 안됨!
# 예로 계산기 프로그램을 실행시켰을 때, 마지막 사용하고 닫았을 때의 위치를 기억해서 다음 실행 시 동일 위치에서 창을 띄운다
# 이런 식으로 현재 실행중인 프로그램의 위치를 받아오고, 받아온 위치를 활용해서 macro 등을 실행시킬 수 있다

import pyautogui

# fw = pyautogui.getActiveWindow()    # fw : Forground Window; 현재 활성화된 창
# print(fw.title)     # >>> 7_window.py - Python_Study - Visual Studio Code   # 창의 제목 정보
# print(fw.size)                              # >>> Size(width=1280, height=1032)
# print(fw.left, fw.top, fw.right, fw.bottom) # >>> 1920 0 3200 1032  : 창의 좌표 정보
# pyautogui.click(fw.left + 45, fw.top + 15)  # 활성화된 창의 정보를 기준으로, 좌표를 지정할 수 있다

# for w in pyautogui.getAllWindows():
#     if w.isActive:  # 모든 윈도우 중에서 Active된 애들만 걸러서 돌리기
#         print(w)    # 모든 윈도우 가져오기  (결과 보니 Background 프로그램도 모두 가져오는 것 같음)

# for w in pyautogui.getWindowsWithTitle("제목 없음"):    # Window Title에 "제목 없음" 이 포함된 애들을 받아옴 (ex) 그림판, 메모장)
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:     # 만약 해당 창이 활성화되지 않은 상태일 경우,
    w.activate()            # 해당 window를 활성화한다 (= 맨 위로 올린다.. 활성화는 되는데 올라오진 않음)


# https://www.youtube.com/watch?v=exgO1LFl9x8&t=9466s
# 3:31:43
