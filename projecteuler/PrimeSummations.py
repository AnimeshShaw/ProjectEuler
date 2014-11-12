import time
start = time.time()

def sieve(num):    
    primes, s = [], [True] * (num + 1)
    for p in range(2, num + 1):
        if s[p]:
           primes.append(p)
           for i in range(p * p, num + 1, p):
               s[i] = False
    return primes

primes=sieve(1000)
targetVal=2
while True:
    numOfWays = [1]+[0]*targetVal
    for i in primes:
        for j in range(i, targetVal+1):
            numOfWays[j] += numOfWays[j-i]
    if numOfWays[targetVal] > 5000:
        break
    targetVal += 1;

print targetVal
print "Run Time = " + str(time.time() - start)
