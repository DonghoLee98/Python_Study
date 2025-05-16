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

Label(root, text="메뉴를 선택해 주세요", height=2).pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="베토디").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="빅맥").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.attributes('-topmost', True)   # 모든 창 위에 표시, False면 일반 창으로 동작

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌
