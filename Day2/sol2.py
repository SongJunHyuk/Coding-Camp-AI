def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    for i in reversed(range(n)) :
       if(sieve[i]) :
          return i
          break

prime_list(99258236)