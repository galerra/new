from random import randint
array = []
N = 28
minimum = 101
for i in range(N):
    number = randint(0, 100)
    array.append(number)

for i in array:
    if i >= 40 and i < minimum:
        minimum = i
print(minimum)







