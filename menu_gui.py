from decimal import MIN_ETINY
from textwrap import indent
from tkinter import *
import random
from PIL import ImageTk,Image

# 1. 루트화면 (root window) 생성
tk = Tk()

menuDB = ["짜장면", "짬뽕", "탕슉"]

label = Label(tk,text='AI가 추천해주는 메뉴는?') 
label.pack()

labelImage = Label(tk, image=None)
labelImage.pack()

photo1 = ImageTk.PhotoImage(Image.open("./image/짜장면.png"))
photo2 = ImageTk.PhotoImage(Image.open("./image/짬뽕.png"))
photo3 = ImageTk.PhotoImage(Image.open("./image/탕슉.png"))

def event():
    menu = random.choice(menuDB)
    button['text'] = menu
    if menuDB.index(menu) == 0:
        labelImage.configure(image=photo1)
    elif menuDB.index(menu) == 1:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)

button = Button(tk,text='메뉴 추천',command=event)
button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button2.pack(side=LEFT, padx=10, pady= 10)

# 4. 메인루프 실행
tk.mainloop()