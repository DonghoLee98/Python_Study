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


root.attributes('-topmost', True)   # 모든 창 위에 표시, False면 일반 창으로 동작

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌
