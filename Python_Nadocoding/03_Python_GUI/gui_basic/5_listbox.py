# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *   

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

# selectmode="extended" : 복수 선택 가능 / "single" : 단일 선택만 가능
# height=0 : list의 모든 내용을 한 번에 display / =n : n개 만큼만 display -> scroll bar와 연계 사용
listbox = Listbox(root, selectmode="extended", height=0)
# list에 순서를 지정해서 값을 넣거나
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "버내나")
# END 로 list 맨 마지막에 넣는 방법도 있다
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0)   # 맨 처음 내용 삭제
    # listbox.delete(END) # 맨 뒤 내용 삭제

    # 개수 확인
    # print("현재 리스트에", listbox.size(), "개가 있어요")

    # 항목 확인
    # print("1 ~ 3 번째 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (idx 넘버(위치)로 반환)
    # print("선택된 항목 : ", listbox.curselection())

    # +@ idx 넘버 말고 내용 출력
    selected_indicies = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indicies]
    print("선택된 항목 : ", selected_items)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌