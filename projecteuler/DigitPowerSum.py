"""
@author Psycho_Coder
"""
def digitsum(num):
    return sum(map(int, num))

data = []

for base in range(7, 80):
    for expo in range (2, 10):
        temp = base ** expo
        if digitsum(str(temp)) == base:
            data.append(temp)
            print("{0}^{1} = {2}".format(base, expo, temp))
print(sorted(data)[29])
