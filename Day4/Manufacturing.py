#Step 0

#Step 1

#새로운 list


#정렬
def srt(s):
    s = list(s)
    s.sort(reverse=False)
    return ''.join(s)

# 조합의 길이를 측정하기 위한 변수 x
def sol1(partNames, RM) :
    list1 = partNames.copy()
    x = 0
    while x < len(partNames)-1 :
        x+=1
        # list를 돌기위한 변수 t
        for t in range (len(list1)) :
            #조합의 길이를 점차 늘려가가기 위한 조건 / 글자수가 조건에 부합할 때
            if(len(list1[t]) == x) :
                #2글자 이상일때를 위한 변수 k
                for k in range(len(list1[t])) :
                    #확인을 위한 탐색용 변수 P
                    for p in partNames :
                        #해당하는 값을 찾고싶을때
                        if (list1[t][k] == p) :
                            #관계행렬을 돌기 위한 변수 i
                            for i in range(len(partNames)) :
                                #RM[변수자리][1을 찾기위한 위치]
                                if(RM[ord(p)-65][i] == 1) and (partNames[i] not in list1[t]) :
                                    tmp = list1[t] + partNames[i]
                                    tmp2 = srt(tmp)
                                    if not tmp2 in list1 :
                                        list1.append(tmp2)

    return list1

#Step 2
def sol2(partNames, list1) :
    list2 = []

    result = ""
    #1일때 예외 지정
    for y in range(len(partNames)) :
        result += partNames[y]
        if(y < len(partNames)-1) :
            result += "/"
    list2.append(result)

    #글자수 측정
    for x in list1 :
        if(len(x) >= 2 and len(x) <= 4) :
            result = ""
            result += x
            for c in partNames :
                if(c not in x) :
                    result += "/"
                    result += c
            list2.append(result)
    return list2

#Step 3

def sol3(partNames, list2) :

    #초기화
    result = [[0 for j in range(len(list2))] for i in range(len(list2))]


    for y in range(len(list2)) :
        left = list2[y].split('/')
        for x in range(len(list2)) :
            cnt = 0
            up = list2[x].split('/')
            #2일때
            if(len(up[0]) == 2) and (len(up[0]) > len(left[0])) :
                result[y][x] = 1
            #2이상일때
            elif(len(up[0]) > 2) :
                #글자하나 차이
                if(len(left[0]) == (len(up[0]) - 1)) :
                    tmpList = []
                    for i in partNames :
                        if( i in left[0]) :
                            tmpList.append(i)

                    for p in up[0] :
                        if p in tmpList :
                            cnt+=1
                                
                    if((cnt+1) == len(up[0])) :
                        result[y][x] = 1
    return result

def main() :
    partNames= ['A', 'B', 'C', 'D']

    RM = [[0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]]

    print(partNames)
    print(RM)
    print()

    list1 = sol1(partNames, RM)
    print(list1)

    list2 = sol2(partNames, list1)

    print()
    print(list2)

    print()
    list3 = sol3(partNames, list2)

    for i in range (len(list3)) :
        print(list3[i])

main()