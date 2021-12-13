import tkinter as tk
import tkinter.font
import tkinter.filedialog as fd
import pandastable as ps
import pandas as pd
import ntpath

# df_left = pd.read_csv("C:/Users/CRS-P-135/Desktop/Study/Study_01/Study_01_DB Specification_V2.2.csv", encoding = "CP949")
# df_right = pd.read_csv("C:/Users/CRS-P-135/Desktop/SDTM.csv", encoding = "CP949")
df_left = pd.DataFrame([None])
df_right = pd.DataFrame([None])

csv_path_list = []

cnt = 0
temp = None

#프레임만 있어도 path받아올 수 있음 굳이 tkinter 안써도 됨.
#어쩌피 csv 경로만 가져올 것이기 때문.
window = tk.Tk()   #생성구문 -> 가장 상위 레벨의 윈도우 창 생성

def Browse():
    path = fd.askopenfilename(initialdir = '/', title = "파일 탐색기", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
    if path not in csv_path_list:
        csv_path_list.append(path)
        csv_list.insert("end", ntpath.basename(path))

def Selection(event):
    selection = csv_list.curselection()     #curseselection은 line number 반환해줌
    if len(selection) == 0:
        return

    global df_left, df_right, cnt, table_after, table_before, temp

    if selection != temp:
        df_left = pd.read_csv(csv_path_list[selection[0]], encoding = "CP949")
        df_right = pd.read_csv(csv_path_list[selection[0]], encoding = "CP949")
        cnt+=1
        print(cnt)
        table_before = ps.Table(frame5, dataframe = df_left)
        table_before.show()
        table_after = ps.Table(frame6, dataframe = df_right)
        table_after.show()
    temp = selection


def Convert():
    '''
    1. df1을 EDC to SDTM convert method 사용(먼저 저장하는 식이 아니기에 df1을 복사한 후 복사본을 수정)
    2. Convert 완료한 것
    3. SDTM mapping rule 새로운 window창으로 켜기
    '''

    pass

def Contact():

    Contact_window = tk.Tk()
    Contact_window.iconbitmap("C:/Users/CRS-P-135/Desktop/20211130_162430.ico")
    Contact_window.title("Contact")  # 프로그램 창의 이름
    Contact_window.geometry("500x300+100+100")  # 프로그램 크기, 위치
    Contact_window.resizable(False, False)  # 프로그램 창 가로, 세로 조정 해도 되는지

    label = tk.Label(Contact_window, text = "If you have any questions,\n contact me via jmhan@crscube.io", font = tk.font.Font(size = 20, weight = "bold"), relief = "flat")
    label.place(x = 120, y = 120)

    Contact_window.mainloop()

def Save():
    path = csv_path_list[temp[0]][:-4]
    df_right.to_csv(path+"_new.csv", encoding = "euc-kr", index = False)



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

window.iconbitmap("C:/Users/CRS-P-135/Desktop/20211130_162430.ico")
window.title("EDC To SDTM") #프로그램 창의 이름
window.geometry("1280x800+100+100")  #프로그램 크기, 위치
window.resizable(True, True)    #프로그램 창 가로, 세로 조정 해도 되는지
window.configure(bg = 'beige')


frame1 = tk.Frame(window, bd=2, bg = "beige")
frame1.pack(side = "left", fill = "y")

frame2 = tk.Frame(frame1, bd=2, bg = "beige")
frame2.pack(side = "top", fill = "y", expand = True)

frame3 = tk.Frame(frame1, bd=2, bg = "beige")
frame3.pack(side = "bottom", anchor = "w")


'''
Buttons
'''
convert_button = Button(frame_num = 3, text = "Convert")
# convert_button.button.config(window = frame1)
convert_button.button.pack(side = "left", fill = "y")

save_button = Button(frame_num = 3, text = "Save")
# save_button.button.config(window = frame1)
save_button.button.pack(side = "right", fill = "y")
save_button.button.config(command = Save)

# if convert_button.cget("state") == "active":





csv_list = tk.Listbox(frame2, selectmode = "extended")
csv_list.pack(side = "left", fill = "y")
csv_scrollbar = tk.Scrollbar(frame2, orient = "vertical", command = csv_list.yview)
csv_scrollbar.pack(side = "left", fill = "y")
csv_list.config(yscrollcommand = csv_scrollbar.set)
csv_list.bind("<<ListboxSelect>>", Selection)
#listbox.insert로 라벨 넣음 -> 각 csv 들어올 때 마다 파일명 이름으로 insert해주면 될 듯함.

# for i in range(1, 101):
#     csv_list.insert(i, str(i)+".csv")

frame4 = tk.Frame(window, bd = 2, bg = "beige")
frame4.pack(side = "top", fill = "y", anchor = "w")

label_convert = tk.Label(frame4, text = "Which data do you want to convert?  ", font = tk.font.Font(size = 18, weight = "bold"), relief = "flat", bg = "beige")
label_convert.pack(side = "left", anchor = "w")


data_browse_button = Button(frame_num = 4, text = "Browse")
data_browse_button.button.pack(side = "right", anchor = "e")
data_browse_button.button.config(command = Browse)




filter_word = tk.StringVar()
filtering_area = tk.Entry(window, textvariable = filter_word, width = 150).pack(side = "top", fill = "y", anchor = "w")


frame7 = tk.Frame(window, bd = 2, bg = "beige")
frame7.pack(side = "bottom", fill = "x")

frame8 = tk.Frame(frame7, bd = 2, bg = "beige")
frame8.pack(side = "left", fill = "both", expand = True)

frame9 = tk.Frame(frame7, bd = 2, bg = "beige")
frame9.pack(side = "right", fill = "both", expand = True)

label_before = tk.Label(frame8, text = "Before", font = tk.font.Font(size = 18, weight = "bold"), relief = "flat", bg = "beige")
label_before.pack()

label_after = tk.Label(frame9, text = "After", font = tk.font.Font(size = 18, weight = "bold"), relief = "flat", bg = "beige")
label_after.pack()


frame5 = tk.Frame(window, bd=2, bg = "beige")
frame5.pack(side = "left", fill = "both", expand = True)

table_before = ps.Table(frame5, dataframe = df_left)
table_before.show()

frame6 = tk.Frame(window, bd=2, bg = "beige")
frame6.pack(side = "right", fill = "both", expand = True)

table_after = ps.Table(frame6, dataframe = df_right)
table_after.show()

'''
Menus
'''

menubar = tk.Menu(window)

menu_files = tk.Menu(menubar, tearoff = 0)
menubar.add_command(label = "Open")
menubar.add_command(label = "Save")
menubar.add_cascade(label = "Files", menu = menu_files)


menu_help = tk.Menu(menubar, tearoff = 0)
menu_help.add_command(label = "Contact", command = Contact)
menubar.add_cascade(label = "Help", menu = menu_help)


window.config(menu = menubar)

window.mainloop()   #반복구문 -> 윈도우 창을 윈도우가 종료될 때까지 실행
