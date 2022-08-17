N = int(input("N을 입력하시오"))

a = 0
b = 1
c = 2

def check(a, b, c) :
    tmp = False
    if(a < b and b < c) :
        if(c**2 == (b**2 + a**2)) :
            if(a+b+c == N) :
                tmp = True
                return tmp
    else :
        return tmp

for c in range (N) :
    for b in range (c) :
        for a in range (b) :
            if(check(a, b, c)) :
                print(a*b*c)
                break
            