# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *

root = Tk()
root.title("DH GUI")

window_width = 640
window_height = 480

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# root.geometry("640x480")

    # btn1 = Button(root, text="버튼1")
    # btn2 = Button(root, text="버튼2")

    # # pack의 속성값으로 처리하면 화면 전체를 기준으로 위치를 잡는다.
    # # btn1.pack(side="left")
    # # btn2.pack(side="right")

    # # grid를 사용해서 위치를 데카르트 좌표로 지정해 준다
    # btn1.grid(row=0, column=0)
    # btn2.grid(row=1, column=1)

# Apple 제품 중 텐키 있는 키보드 배열 표현
# 최상단 줄
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="sub", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="add", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1 시작 줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)  # 세로로 2 칸 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)  # 현재 위치로부터 아래쪽으로 줄을 더함

# 0 시작 줄
btn_0 = Button(root, text="0", width=5, height=2)  # 가로로 합쳐짐
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)   # 현재 위치로부터 오른쪽으로 column을 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.attributes('-topmost', True)   # 모든 창 위에 표시, False면 일반 창으로 동작

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌
