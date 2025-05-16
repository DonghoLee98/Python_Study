# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file=r"C:\IT_Study\Python_Study\Python_Nadocoding\03_Python_GUI\gui_basic\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="bye")

    global photo2   # photo2 를 전역변수로 지정하지 않으면 Garbage Collection에 의해 지워진다!
    photo2 = PhotoImage(file=r"C:\IT_Study\Python_Study\Python_Nadocoding\03_Python_GUI\gui_basic\img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌