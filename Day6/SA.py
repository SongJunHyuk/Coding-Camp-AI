import csv
import math
import random
import matplotlib.pyplot as plt
import time

#거리를 계산하여 담을 list, 방문처리할 list 선언

#파일 생성
fields = []
rows = []

#거리 구하기
def distance(x1,y1, x2,y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    return (math.sqrt(xdiff*xdiff + ydiff*ydiff))

#현재부터 거리구하기, 방문 기록
def calDist(rows, cx, cy, vlist, dlist) :
    for i in range(len(vlist)) :
        if(vlist[i] == False) :
            dlist[i] = distance(cx,cy,float(rows[i+1][1]),float(rows[i+1][2]))

#row에 이중 리스트로 데이터 저장
with open('Input_data.csv', 'r') as csvfile:
    rdr = csv.reader(csvfile)
      
    fields = next(rdr)
  
    for row in rdr:
        rows.append(row)

#초기화
currentx = float(rows[0][1])
currenty = float(rows[0][2])
T0 = 100000
cool = 5
Tfianl = 0
cot= 0
result = []
global XL_B 
#main

def Zfunc(Xlist) :

    Dist = 0
    cx = float(rows[0][1])
    cy = float(rows[0][2])

    for i in range(len(Xlist)-1) :

        Dist += distance(float(rows[int(Xlist[i+1])][1]), float(rows[int(Xlist[i+1])][2]), cx, cy)
        
        cx = float(rows[int(Xlist[i+1])][1])
        cy = float(rows[int(Xlist[i+1])][2])
        
    return Dist

#99번 반복
def greedy(sum, result, rows, currentx, currenty) :
    
    vlist = [False for i in range(99)]
    dlist = [0 for i in range(99)]  
    sum = 0
    result.append(rows[0][0])

    for r in range(len(vlist)) :
        m = float("inf")
        #거리계산
        for k in range(len(vlist)) :
            if(vlist[k] == False) : 
                calDist(rows, currentx, currenty, vlist, dlist)

        #최소값찾기
        for j in range(len(vlist)) :
            if((vlist[j] == False) and float(dlist[j]) < m) :
                m = dlist[j]

        for a in range(len(vlist)) :
            if(vlist[a] == False) and (dlist[a] == m):
                i = dlist.index(m)

        sum += m
        vlist[i] = True
        dlist[i] = float("inf")
        currentx = float(rows[i+1][1])
        currenty = float(rows[i+1][2])
        result.append(rows[i+1][0])
    sum += distance(currentx, currenty, float(rows[0][1]), float(rows[0][2]))
    result.append(rows[0][0])
    return sum, result

#Swap
def swap(XL, K) :
    global XL_B
    XL_B = XL.copy()
    d1 = random.randrange(1,100)
    d2 = random.randrange(1,100)
    XL_B[d1], XL_B[d2] = XL_B[d2], XL_B[d1]
    return XL_B, XL

#validtation check
def check(Xtmp, Xtt) :
    global Xcur
    global Zcur
    global Xbest
    global Zbest
    global Tcur
    if(Zfunc(Xtmp) < Zcur) :
        Xcur = Xtmp
        Zcur = Zfunc(Xtmp)
    else :
        dlC = Zfunc(Xtmp) - Zcur
        if(random.random() < math.exp(1)**(-(dlC/Tcur))*0.0005) :
            Xcur = Xtmp
            Zcur = Zfunc(Xtmp)
    if(Zfunc(Xcur) < Zbest) :
        Xbest = Xcur
        Zbest = Zfunc(Xcur)
        return Xtmp
    return Xtt
    

#main init
Z0, X0 = greedy(sum, result, rows, currentx, currenty)
global Xcur
Xcur = X0
global Zcur
global Tcur
global Xbest
global Zbest
Zcur = Zfunc(Xcur)
Tcur = T0
Xbest = Xcur
Zbest = Zcur
Tfianl = 0
Xt = X0
curlist = []
bestlist = []
Templist = []
#main

while (Tcur > Tfianl) :
    #Step2
    Xtp, Xt = swap(Xt, Tcur)
    Xt = check(Xtp, Xt)
    #종료조건
    Tcur = Tcur - cool
    curlist.append(Zfunc(Xcur))
    bestlist.append(Zbest)
    Templist.append(Tcur)
# print(Z0, X0)

print("Distance :" + str(Zbest))
print("Route :" + str(Xbest))
print("length : " + str(len(Xbest)))
print()
plt.plot(Templist, curlist, "b^")
plt.plot(Templist, bestlist, "ro")
plt.legend(['current', 'best'])
plt.xlabel('Temperature')
plt.ylabel('Distance')
plt.gca().invert_xaxis()
plt.rcParams["figure.figsize"] = (3,5)
plt.show()

csvfile.close()