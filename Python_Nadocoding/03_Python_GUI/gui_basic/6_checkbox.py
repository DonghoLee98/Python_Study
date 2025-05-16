# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

chkvar = IntVar()   # chkver에 int형으로 값을 저장한다!
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()     # chkbox 체크여부 "V" default 지정
# chkbox.deselect()   # chkbox 체크여부 " " default 지정
chkbox.pack()

chkvar2 = IntVar()  # chkvar2 의 값을 저장하기 위해 또다른 변수 만들어 준다
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제 / 1 : 체크 설정
    print(chkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌