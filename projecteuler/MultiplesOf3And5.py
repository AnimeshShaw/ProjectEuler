#Version 1 Bruteforce
print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))

#Version 2 Bruteforce
print(sum(i for i in range(1000) if not i % 3 or not i % 5))

#Version 3 Mathematically Optimized
print(sum(i for i in range(3, 1000, 3)) + sum(i for i in range(5, 996, 5)) - sum(i for i in range(15, 991, 15)))
