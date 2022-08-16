N = int(input('숫자를 입력하시오'))
sum = 0

if (N <= 1000) :
    for x in range(N) :
        if (x%3 == 0 or x%5 == 0) :
            sum += x
    print(sum)
else :
    print("입력값이 잘못되었습니다.")