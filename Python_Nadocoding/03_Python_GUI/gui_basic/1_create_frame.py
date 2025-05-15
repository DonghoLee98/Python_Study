# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")            # 가로x세로
# root.geometry("640x480+100+300")    # 가로x세로+x좌표+y좌표

root.resizable(False, False)        # x(너비), y(높이) 값 변경 불가 (= 창 크기 변경 X)

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌