# tkinter 안의 모든 모듈을 가져다 사용하겠다.
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

# # mode="indeterminate" : 언제 끝날지 계산되지 않음
# # mode="determinate" : 0에서 100까지 차오르는 애니메이션

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)   # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동 중지 (progressbar status 삭제됨)

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)           # progressbar의 값 설정
        progressbar2.update()   # UI 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌