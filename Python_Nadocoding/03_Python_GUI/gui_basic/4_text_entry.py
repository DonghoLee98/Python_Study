# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

# text 위젯 안에 미리 Hint text를 적어둔다! (클릭 시 지워지지는 않음)
txt.insert(END, "글자를 입력하세요")

# text와 유사하나, 줄바꿈을 할 수 없다
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요") # 값이 비어있으므로 0이나 END나 동일하다

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1.0 : 1번 라인, 0 번째 column 부터 / END : 마지막까지 가져와라
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌