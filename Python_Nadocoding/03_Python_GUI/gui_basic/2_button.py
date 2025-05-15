# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")

btn1 = Button(root, text="버튼1")   # 버튼 만들고
btn1.pack()                         # pack에 포함시켜 GUI로 우리가 볼 수 있게 함

# padx & pady : 좌우 & 상하 여백
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width & height : 고정된 크기기
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file=r"C:\IT_Study\Python_Study\Python_Nadocoding\03_Python_GUI\gui_basic\img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭 되었습니다!")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

# https://www.youtube.com/watch?v=bKPIcoou9N8&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=3
# 17:00


root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌