# tkinter 안의 모든 모듈을 가져다 사용하겠다.
from tkinter import *

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 생성합니다")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disabled")   # 해당 메뉴 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)  # 리본메뉴 추가

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 (radio 버튼으로 확인)
menu_lang = Menu(menu, tearoff=0)

default_lang = StringVar(value="Python")    # +@ Default 값 지정 (아래 value= 와 link)

menu_lang.add_radiobutton(label="Python", variable=default_lang, value="Python")
menu_lang.add_radiobutton(label="Java", variable=default_lang, value="Java")
menu_lang.add_radiobutton(label="C++", variable=default_lang, value="C++")

menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)  # Main Window에 menu를 포함시킨다
root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌