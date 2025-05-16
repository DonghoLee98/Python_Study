# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

# 한 줄 코드. Label 값을 활용하려면 label1 = ~~ 이런식으로 변수에 따로 할당해야 함
Label(root, text="메뉴를 선택하세요").pack()

# Radiobutton : 여러 항목 중 택 1
burger_var = IntVar()   # int형 값 저장 (chkbox와 다르게 이걸 "그룹"으로 공유한다)
btn_burger1 = Radiobutton(root, text="베토디", value=1, variable=burger_var)
btn_burger1.select()    # 선택 default 지정, 마지막 실행 코드의 변수를 default로 최종 지정한다
btn_burger2 = Radiobutton(root, text="빅맥", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="맥스파이시", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="음료를 선택하세요").pack()

drink_val = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_val)
btn_drink1.select() # 기본값 설정
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_val)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 radio 항목의 값을 출력
    print(drink_val.get())  # 음료 중 선택된 값 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌