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

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# yscrollcommand=scrollbar.set 로 scrollbar와 매핑하기
listbox = Listbox(frame, selectmode="extended", height = 10, yscrollcommand=scrollbar.set)
for i in range(1, 32):  # 1 ~ 31일 사이
    listbox.insert(END, str(i) + "일")  # listbox의 리스트 마지막에 1일, 2일 ... 추가
listbox.pack(side="left")

# command=listbox.yview 로 listbox와 매핑하기
scrollbar.config(command=listbox.yview)

root.attributes('-topmost', True)   # 모든 창 위에 표시, False면 일반 창으로 동작

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌
