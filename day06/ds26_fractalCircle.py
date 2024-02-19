# file : ds26_fractalCircle.py
# desc : 프랙탈 원 그리기, 프랙탈 : 삼각형, 사각형, 원 등의 구조를 자기 복제 형태로 반복해서 구성

from tkinter import *
import random

def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    if r >= 5:  # 반지름이 5 이상일 때까지 반복
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

# 전역변수
radius = 400
wSize = 1000
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet', 'crimson', 'azure', 'gray']

# 메인코드
window = Tk()
window.title('프랙탈 원 그리기')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')


drawCircle(wSize//2, wSize//2, radius)
canvas.pack()

window.mainloop()