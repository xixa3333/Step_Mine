from tkinter import *
from functools import partial
import random
import os
from PIL import Image, ImageTk
import sys

def resource_path(relative_path):
    """獲取打包後的資源路徑"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

root = Tk()
root.title("踩地雷")

Max = 0
timer = None
time = 0
Flag_Num = 0
Start_Flag = 0
Boom_Num = 0
Remaining_Blocks = 0
TOTAL_IMAGES = 12  # 總圖像數量

# 圖片目錄與檔名
image_folder = resource_path("image")
image_files = ['blank.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','0.png','flag.png','mines.png']
images = []
# 指定大小
IMG_SIZE = (25,25)  # 寬度 x 高度
for file in image_files:
    path = os.path.join(image_folder, file)
    img = Image.open(path).resize(IMG_SIZE, Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    images.append(img_tk)

department=["簡單","普通","困難"]

Blocks = [[None] * Max for _ in range(Max)]
Mine_Detection = [[0] * Max for _ in range(Max)]
Flag_Record = [[0] * Max for _ in range(Max)]

Difficulty = StringVar()
Time_Label=StringVar()
Flag_Num_Label=StringVar()
Start_Label=StringVar()

Difficulty.set("簡單")
Time_Label.set('時間：0')
Flag_Num_Label.set('旗子數:0')
Start_Label.set("開始")

def data(Max_Temp,Flag_Num_Temp):
    global Max,Flag_Num,Boom_Num
    Max = Max_Temp
    Flag_Num = Flag_Num_Temp
    Boom_Num = Flag_Num_Temp

def Spawning_Mines(y,x):
    placed = 0

    forbidden = set()  # 不允許有地雷的位置
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_y = y + i
            new_x = x + j
            if 0 <= new_y < Max and 0 <= new_x < Max:
                forbidden.add((new_y, new_x))

    while placed < Boom_Num:
        X = random.randint(0, Max-1)
        Y = random.randint(0, Max-1)

        if (Y, X) in forbidden:
            continue
        if Mine_Detection[Y][X] == -1:
            continue  # 重複地雷位置

        Mine_Detection[Y][X] = -1  # -1代表地雷

        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y = Y + i
                new_x = X + j
                if 0 <= new_y < Max and 0 <= new_x < Max and Mine_Detection[new_y][new_x] != -1 : 
                    Mine_Detection[new_y][new_x] += 1

        placed += 1

def Touch_Flag(event, y, x):
    global Flag_Record,Flag_Num
    if(Flag_Num == 0):return
    if(Flag_Record[y][x] == 0):
        Flag_Record[y][x] = 1
        tk_img = images[10]
        Flag_Num -= 1
        Blocks[y][x].config(state="disabled")

    elif(Flag_Record[y][x] == 1):
        Flag_Record[y][x] = 0
        tk_img = images[9]
        Flag_Num += 1
        Blocks[y][x].config(state="normal")

    Blocks[y][x].config(image=tk_img)
    Blocks[y][x].image = tk_img
    Flag_Num_Label.set('旗子數:'+str(Flag_Num))

def Touch(y, x):
    global Start_Flag,Remaining_Blocks,Flag_Record,Flag_Num

    if Blocks[y][x]['state'] == "disabled":
        return  # 已打開，無需處理
    
    if(Start_Flag == 0):
        Start_Flag = 1
        Spawning_Mines(y, x)

    if(Flag_Record[y][x] == 1):
        Flag_Record[y][x] = 0
        Flag_Num += 1
        Flag_Num_Label.set('旗子數:'+str(Flag_Num))

    Remaining_Blocks -= 1
    if(Remaining_Blocks == Boom_Num):
        End("成功")

    if(Mine_Detection[y][x] != -1):
        tk_img = images[Mine_Detection[y][x]]
        Blocks[y][x].config(image=tk_img)
        Blocks[y][x].image = tk_img
    
    Blocks[y][x].config(state="disabled")
    Blocks[y][x].unbind("<Button-3>")

    if(Mine_Detection[y][x] == -1):
        End("失敗")

    elif(Mine_Detection[y][x] == 0):
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y = y + i
                new_x = x + j
                if 0 <= new_y < Max and 0 <= new_x < Max:
                    Touch(new_y, new_x)

def Time_End():
    global timer,time
    if timer is not None:
        root.after_cancel(timer)
        timer = None
    time = 0

def End(result):
    for i in range(0, Max):
        for j in range(0, Max):
            if(Mine_Detection[i][j] == -1):
                tk_img = images[11]
                Blocks[i][j].config(image=tk_img)
                Blocks[i][j].image = tk_img
            Blocks[i][j].config(state="disabled")
            Blocks[i][j].unbind("<Button-3>")

    Time_End()
    Start_Label.set(result)

def Return():
    global timer,Blocks,Mine_Detection,Start_Flag,Remaining_Blocks,Flag_Record

    for i in range(0, Max):
        for j in range(0, Max):
            Blocks[i][j].destroy()
    
    Time_End()
    Start_Flag = 0

    if (Difficulty.get() == department[0]) : data(8,10)
    elif (Difficulty.get() == department[1]) : data(14,40)
    elif (Difficulty.get() == department[2]) : data(20,99)

    Blocks = [[None] * Max for _ in range(Max)] # 地雷按鈕
    Mine_Detection = [[0] * Max for _ in range(Max)] # 地雷探測
    Flag_Record = [[0] * Max for _ in range(Max)]

    Remaining_Blocks = Max*Max#剩餘方塊
    Start_Label.set("重置")
    Flag_Num_Label.set('旗子數:'+str(Flag_Num))

    for i in range(0, Max):
        for j in range(0, Max):
            tk_img = images[9]
            Blocks[i][j] = Button(root,state="normal",image=tk_img, command=partial(Touch, i, j))
            Blocks[i][j].grid(row=i+1, column=j)
            Blocks[i][j].image = tk_img
            Blocks[i][j].bind("<Button-3>", lambda e,y=i, x=j: Touch_Flag(e,y, x))

    timer = root.after(1000, change_time)
        
def change_time():
    global time,timer
    time += 1
    
    Time_Label.set('時間：'+str(time))
    timer = root.after(1000, change_time)

def main():
    global Blocks
    
    om=OptionMenu(root, Difficulty, *department)
    om.grid(row=0, column=0,columnspan=3)
    
    Start=Button(root, height=1, textvariable=Start_Label, command=partial(Return))
    Start.grid(row=0, column=3,columnspan=3)

    Time_Label_Obj = Label(root, textvariable=Time_Label, height=2)
    Time_Label_Obj.grid(row=0, column=6, columnspan=2)

    Flag_Num_Label_Obj = Label(root, textvariable=Flag_Num_Label, height=2)
    Flag_Num_Label_Obj.grid(row=0, column=8, columnspan=2)
    
    root.mainloop()

main()
