# file : ds05_orderedList.py
# desc : 선형리스트 응용

def printPoly(p_x):
    term = len(p_x) - 1 # 최고차항 숫자
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]   # 계수

        # 계수 0 출력X, 첫 번째 항 + 출력X로 바꿔보기
        if coef > 0:
            if i != 0:
                polyStr += '+'
            else:
                pass
        elif coef == 0:
            term -= 1
            continue

        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]   # 계수
        retValue += coef * xVal ** term
        term -= 1
    
    return retValue

# 전역 변수
px = [7, -4, 0, 5]      # 7x^3 - 4x^2 + 0x^1 + 5x^0
# px = [0, -4, 0, 5]        # - 4x^2 + 5x^0

if __name__ == '__main__':
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X값 --> "))

    pxValue = calcPoly(xValue, px)
    print(pxValue)