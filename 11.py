from random import randint
array = []
N = 30
s = 0
for i in range(N):
    number = randint(-1000, 1000)
    array.append(number)

for m in array:
    if m >= 0:
        if s == 0:
            s += m
print(s)







