import tkinter as tk
import tkinter.font
import tkinter.filedialog as fd

#프레임만 있어도 path받아올 수 있음 굳이 tkinter 안써도 됨.
#어쩌피 csv 경로만 가져올 것이기 때문.
window = tk.Tk()   #생성구문 -> 가장 상위 레벨의 윈도우 창 생성

def Browse():
    path = fd.askopenfile(initialdir = '/', title = "파일 탐색기", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))

class Button:
    def __init__(self, frame_num, text):
        self.window = eval("frame"+str(frame_num))
        self.text = text
        self.activebackground = "yellow"
        self.borderwidth = 3
        self.font = tk.font.Font(weight = "bold")
        self.button = tk.Button(self.window, text = self.text, activebackground = self.activebackground, borderwidth = self.borderwidth, font = self.font)
        self.button.pack(side = "left")

    # def text(self, text):
    #     self.button.config(text = text)

    # def pack(self, position):
    #     self.button.pack(side = position)


window.title("EDC To SDTM") #프로그램 창의 이름
window.geometry("1280x800+100+100")  #프로그램 크기, 위치
window.resizable(True, True)    #프로그램 창 가로, 세로 조정 해도 되는지


frame1 = tk.Frame(window, bd=2)
frame1.pack(side = "left", fill = "y")


frame0 = tk.Frame(frame1, bd=2)
frame0.pack(side = "bottom", anchor = "w")

frame4 = tk.Frame(frame1, bd=2)
frame4.pack(side = "top", fill = "y", expand = True)


'''
Buttons
'''
convert_button = Button(frame_num = 0, text = "Convert")
# convert_button.button.config(window = frame1)
convert_button.button.pack(side = "left", fill = "y")

save_button = Button(frame_num = 0, text = "Save")
# save_button.button.config(window = frame1)
save_button.button.pack(side = "right", fill = "y")

# if convert_button.cget("state") == "active":







csv_list = tk.Listbox(frame4, selectmode = "extended")
csv_list.pack(side = "left", fill = "y")
csv_scrollbar = tk.Scrollbar(frame4, orient = "vertical", command = csv_list.yview)
csv_scrollbar.pack(side = "left", fill = "y")
csv_list.config(yscrollcommand = csv_scrollbar.set)
#listbox.insert로 라벨 넣음 -> 각 csv 들어올 때 마다 파일명 이름으로 insert해주면 될 듯함.

for i in range(1, 101):
    csv_list.insert(i, str(i)+".csv")





filter_word = tk.StringVar()
filtering_area = tk.Entry(window, textvariable = filter_word, width = 150).pack(side = "top", fill = "y", anchor = "w")



label = tk.Label(window, text = "Which data do you want to convert?", font = tk.font.Font(size = 16, weight = "bold"))
label.pack(side = "bottom")

frame2 = tk.Frame(window, bd=2)
frame2.pack(side = "left", fill = "y")
frame3 = tk.Frame(window, bd=2)
frame3.pack(side = "right", fill = "y")



data_browse_button = Button(frame_num = 2, text = "Browse")
data_browse_button.button.pack(side = "right")
data_browse_button.button.config(command = Browse)


# call_result_1 = partial()
# call_result_2 = partial()


window.mainloop()   #반복구문 -> 윈도우 창을 윈도우가 종료될 때까지 실행
