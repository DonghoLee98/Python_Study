# tkinter 안의 모든 모듈을 가져다 사용하겠다.
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("DH GUI")
root.geometry("640x480")

# ex) 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 되었습니다.")  # ("title", "실제 출력 값")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 예매가 완료되었습니다.\n다른 좌석을 선택해 주세요.")

def error():
    msgbox.showerror("에러", "결제 오류!\n다시 시도해 주세요.")

def okcancel():
    # ok 할지 cancel 할지 User가 선택하도록 한다
    msgbox.askokcancel("확인 취소", "해당 좌석은 유아 동반석입니다.\n계속하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다.\n다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 아니오", "해당 좌석은 역방향입니다.\n그래도 계속하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 종료하시겠습니까?")
    # # 위의 다른 코드 또한 response로 변수를 받아와서 아래처럼 if문 처리하면 동일하게 동작할 수 있다
    # # yes : 저장 후 종료
    # # no : 저장하지 않고 종료
    # # cancel : 이전 화면으로 복귀
    # print("응답", response) # response : True / False / None -> 예 1, 아니오 0, 그 외
    if response == 1:   # 네, ok
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:               # 취소
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()     # pygame 에서와 같이, loop를 통해 창이 닫히지 않게 해줌