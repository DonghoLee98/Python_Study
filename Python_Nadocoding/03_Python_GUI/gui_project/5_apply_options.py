import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *   # __all__
from tkinter import filedialog  # filedialog의 경우 sub module이라 import * 해도 딸려오지 않음!
from PIL import Image

root = Tk()
root.title("DH GUI")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"C:\IT_Study\Python_Study\Python_Nadocoding\03_Python_GUI\gui_project") # tuple 형식, \ : 줄바꿈 처리, C:/ : 최초 경로는 C 드라이브 아래
        # 최초 사용자 지정 경로 보여줌

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제
def del_file():
    # list 앞에서부터 삭제 시 정렬로 인하여 인덱스 순서가 변경됨 -> 뒤에서부터 삭제; reversed(~~)
    # reversed(~~)로 기존의 list data는 남겨두고, reversed된 값을 새로운 곳에 다시 저장해서 활용한다.
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더 선택)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)    # Entry로 처리해서 (0, END). Text로 처리했다면 (1.0, END)로 처리
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():
    # 각 옵션들 값을 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    try:
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1  # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:   # 없음
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower()   # lower() : PNG, JPG, BMP 값을 받아와서 소문자로 변경

        ######################################

        # print(list_file.get(0, END))    # 모든 파일 목록 가져오기
        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []    # [(width1, height1), (width2, height2), ...]
        if img_width > -1:
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식 (가로x세로 길이 비율 맞춰서 사진 크기 변경)
        # 100 * 60 이미지 -> width를 80으로 줄이면 height는?
        # (원본 width) : (원본 height) = (변경 width) : (변경 height)
        # 100 : 60 = 80 : ?
        # ? = (60 * 80) / 100 = 48...
        # ==> 코드에 적용; 
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width        # User가 설정값으로 지정하는 부분
        # y' = x'y / x = img_width * size[1] / size[0]

        widths, heights = zip(*(image_sizes))

        max_width = max(widths)     # max_width : 사진들의 너비 값 중 가장 큰 값 반환
        total_height = sum(heights)

        # 스케치북 준비
        if img_space > 0:   # 이미지 간격 옵션 적용 (전체 도화지 크기 변경경)
            total_height += (img_space * (len(images) - 1))
        
        result_image = Image.new("RGB", (max_width, total_height), (255, 255, 255))  # 배경 흰 색
        y_offset = 0    # 이미지 배치하기 위해 위에서부터 offset 값을 주어 높이를 다르게 배치한다

        for idx, img in enumerate(images):
            # width가 "원본유지" 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_image.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)   # height값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100    # 실제 percent 정보를 계산 (idx가 0부터 시작 -> +1)
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "dh_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_image.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다!")
    
    except Exception as err:    # 예외처리 (폴더 접근 권한, 존재하지 않는 경로 등을 모두 포함)
        msgbox.showerror("에러", err)

# 시작
def start():
    # 파일 목록 확인; 선택된 사진 파일이 없을 경우 msgbox 띄워 사용자에게 warning
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인; 저장 경로 text의 길이 == 0 이면 return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return
    
    # 이미지 통합 작업
    merge_image()


# 파일 프레임 ; 파일 추가, 선택 삭제
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)  # ipady; 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 Label
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5) # 왼쪽부터 오른쪽으로 쌓아나가면서 만들기 위함

# 가로 넓이 Combo
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 Label
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 Combo
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 Label
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 Combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황; progress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)

root.mainloop()