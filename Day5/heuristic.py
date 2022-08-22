import csv
import math
import random
import matplotlib.pyplot as plt

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
sum = 0
result = []
result.append(rows[0][0])

#main

#99번 반복
def greedy(sum, result, rows, currentx, currenty) :

    currentx = float(rows[0][1])
    currenty = float(rows[0][2])
    vlist = [False for i in range(99)]
    dlist = [0 for i in range(99)]  
    rsum = 0
    result = []
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

def rand(rows) :
    currentx = float(rows[0][1])
    currenty = float(rows[0][2])
    blist = [False for i in range(99)]
    rsum = 0
    rresult = []
    rresult.append(rows[0][0])

    for r in range(len(blist)) :
        tmp = random.randrange(0,99)
        #거리계산
        if(blist[tmp] == False) :
            rsum += distance(float(rows[tmp+1][1]),float(rows[tmp+1][2]) , currentx, currenty)
            rresult.append(rows[tmp+1][0])
            currentx = float(rows[tmp+1][1])
            currenty = float(rows[tmp+1][2])
        else :
            r -= 1

    rsum += distance(currentx, currenty, float(rows[0][1]), float(rows[0][2]))
    rresult.append(rows[0][0])
    return(rsum, rresult)

#랜덤 함수
flist = []
slist = []

ga, gb = greedy(sum, result, rows, currentx, currenty)
ra, rb = rand(rows)
print("greedy Distance : "+str(ga))
print("greedy route :" + str(gb))
print()

for z in range(10) :
    ga, gb = greedy(sum, result, rows, currentx, currenty)
    ra, rb = rand(rows)
    
    print("random Distance : " + str(ra))
    print("random route"+ str(z+1) + ": " + str(rb))
    print()
    flist.append(ga)
    slist.append(ra)

plt.plot(slist, "b^")
plt.plot(flist, "ro")
plt.legend(['random', 'greedy'])
plt.xlabel('10 times')
plt.ylabel('Distance')
plt.show()

csvfile.close()