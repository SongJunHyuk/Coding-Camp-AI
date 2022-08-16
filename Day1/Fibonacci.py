pre = 0
cur = 1
Sum = 0
next = 0

while next < 1000000 :
    next = cur + pre
    pre = cur
    cur = next
    if(cur % 2 == 0) :
        Sum += cur
print(Sum) 