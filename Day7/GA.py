import csv
import math
import random
import matplotlib.pyplot as plt

#거리 구하기(좌표)
def distance(x1,y1, x2,y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    return (math.sqrt(xdiff*xdiff + ydiff*ydiff))

#현재부터 거리구하기, 방문 기록
def calDist(rows, cx, cy, vlist, dlist) :
    for i in range(len(vlist)) :
        if(vlist[i] == False) :
            dlist[i] = distance(cx,cy,float(rows[i+1][1]),float(rows[i+1][2]))

#평균 구하기
def avg(flist) :
    result = (sum(flist)/len(flist))
    return result

#랜덤으로 경로 가져오기
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

#거리 구하기(경로 -> 거리)
def Zfunc(Xlist) :

    Dist = 0
    cx = float(rows[0][1])
    cy = float(rows[0][2])

    for i in range(len(Xlist)-1) :

        Dist += distance(float(rows[int(Xlist[i+1])][1]), float(rows[int(Xlist[i+1])][2]), cx, cy)
        
        cx = float(rows[int(Xlist[i+1])][1])
        cy = float(rows[int(Xlist[i+1])][2])
        
    return Dist

#파일 생성
fields = []
rows = []

#row에 이중 리스트로 데이터 저장
with open('Input_data.csv', 'r') as csvfile:
    rdr = csv.reader(csvfile)
      
    fields = next(rdr)
  
    for row in rdr:
        rows.append(row)

#Step1 - Initialization
global M
N = 1000
M = 0
P0 = []
F0 = []

for tm in range(N) :
    initSum , initResult = rand(rows)
    P0.append(initResult)
    F0.append(initSum)

global Pcur
global Fcur
global favg
global fbest
global pBest
global opt

Pcur = P0
Fcur = F0

favg = avg(Fcur)
fbest = min(Fcur)
pBest = Pcur[Fcur.index(fbest)]
opt = fbest
city = len(Pcur[0]) - 1

t1 = 0.7
t2 = 0.3

#Step2 - Selection
def compare(r1, r2) :
    if(Zfunc(r1) < Zfunc(r2)) :
        return r1, r2
    else :
        return r2, r1

def Selection(a1, a2) :
    better , worse = compare(a1, a2)
    if(random.random() < t1) :
        return better
    else :
        return worse

#Step3 - crossover
def crossover(p1, p2) :
    offspring1 = []
    offspring1.append(p1[0])
    offspring2 = []
    offspring2.append(p1[0])
    tmpList1 = []
    tmpList2 = []

    s31 = 1
    s32 = 1

    standard1 = random.randrange(1, city)
    standard2 = random.randrange(1, city)

    while(s31 < city) :
        if(s31 < standard1) :
            offspring1.append(p1[s31])
        else :
            tmpList1.append(p1[s31])
        s31 += 1
    random.shuffle(tmpList1)
    for ss in range(len(tmpList1)) :
        offspring1.append(tmpList1[ss])
    
    while(s32 < city) :
        if(s32 < standard2) :
            offspring2.append(p2[s32])
        else :
            tmpList2.append(p2[s32])
        s32 += 1
    random.shuffle(tmpList2)
    for sw in range(len(tmpList2)) :
        offspring2.append(tmpList2[sw])
    
    offspring1.append(p1[city])
    offspring2.append(p2[city])

    return offspring1, offspring2

#Step4 - Mutation
def mutation(listX) :
    if(random.random() < t2) :
        d1 = random.randrange(1,city)
        d2 = random.randrange(1,city)
        listX[d1], listX[d2] = listX[d2], listX[d1]
    return listX

#Step5 - Update
def Update(offspring1, offspring2) :

    global Pcur
    global Fcur
    global favg
    global fbest
    global pBest
    global opt
    global M
    if(Zfunc(offspring1) < favg) :
        Pcur.append(offspring1)
        Fcur.append(Zfunc(offspring1))
        fworstIndex = Fcur.index(max(Fcur))
        del Pcur[fworstIndex: fworstIndex+1]
        del Fcur[fworstIndex: fworstIndex+1]

    if(Zfunc(offspring2) < favg) :
        Pcur.append(offspring2)
        Fcur.append(Zfunc(offspring2))
        fworstIndex = Fcur.index(max(Fcur))
        del Pcur[fworstIndex: fworstIndex+1]
        del Fcur[fworstIndex: fworstIndex+1]

    favg = avg(Fcur)
    fbest = min(Fcur)

    fIndex = Fcur.index(fbest)
    pBest = Pcur[fIndex]
    opt = min(opt, fbest)
    M+=1

#main
while(fbest > 510) :
    #Step2
    randomA = random.randrange(1, N)
    randomB = random.randrange(1, N)
    parrent1 = Selection(Pcur[randomA], Pcur[randomB])
    parrent2 = Selection(Pcur[randomA], Pcur[randomB])

    #Step3
    o1, o2 = crossover(parrent1, parrent2)

    #Step4
    mutation(o1)
    mutation(o2)

    #Step5
    pIndex1 = Pcur.index(parrent1)
    pIndex2 = Pcur.index(parrent2)

    Update(o1, o2)
    print("favg : " + str(favg))
    print("fbest : " + str(fbest))
    print("opt : " + str(opt))
    print()
    
print("route : " + str(pBest))
print("distance" + str(fbest))

print()
plt.plot(M, favg, "go")
plt.plot(M, fbest, "bo")
plt.plot(M, opt, "ro")
plt.legend(['favg', 'fbest', 'opt'])
plt.xlabel('Generation')
plt.ylabel('Distance')
plt.gca().invert_xaxis()
plt.show()

csvfile.close()