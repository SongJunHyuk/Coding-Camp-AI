polite, info = map(int, input().split())

red = set()
blue = set()
tmp = True
cm = 0
result = 0
friendList = {}
enemyList = {}

def checkFList() :
    for key, value in friendList.items() :
        if(key in red or value in red) :
            red.add(key)
            red.add(value)
        elif(key in blue or value in blue) :
            blue.add(key)
            blue.add(value)

def checkEList() :
    for key, value in enemyList.items() :
        if(key in red or value in blue) :
            red.add(key)
            blue.add(value)
        elif(key in blue or value in red) :
            blue.add(key)
            red.add(value)

for x in range (info) :
    if (x==0) : 
        a, b, c = input().split()
        if(c == 'f') :
            red.add(a)
            red.add(b)
        else :
            red.add(a)
            blue.add(b)
    else :
        a, b, c = input().split()
        if (c == 'f') : 
            if (a in red) or (b in red):
                red.add(a)
                red.add(b)
            elif (a in blue) or (b in blue):
                blue.add(a)
                blue.add(b)
            else :
                friendList[a] = b
        else :
            if a in red or b in blue :
                red.add(a)
                blue.add(b)
            elif b in red or a in blue :
                blue.add(a)
                red.add(b)
            else :
                enemyList[a] = b

    checkFList()
    checkEList()

    if (blue.intersection(red) != set()) :
        if(cm == 0) :
            tmp = False
            result = x+1
            cm+=1

if tmp == True :
    print("THE SPY IS LOYAL")
else :
    print(result)