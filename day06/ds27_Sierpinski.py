# file : ds27_Sierpinski.py
# desc : 시에르핀스키 삼각형 그리기

from tkinter import *
import random

def drawTriangle(x, y, size):
    if size >= 30:
        drawTriangle(x, y, size/2)  # 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2, y, size/2)  # 오른쪽 아래 작은 삼각형
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2)  # 위쪽 작은 삼각형
    # 변의 길이가 30 미만이 되면 삼각형을 그리고 반환(30 미만의 삼각형으로 전체를 채우는 효과)
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill=random.choice(colors), outline='black')

# 전역 변수 선언 부분
wSize = 1000
radius = 400
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet', 'crimson', 'azure', 'gray']

# 메인 코드 부분
window = Tk()
window.title('삼각형 모양의 프랙탈')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
window.mainloop()