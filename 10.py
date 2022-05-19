from random import randint
array = []
N = 20
minim = 1001
for i in range(N):
    number = randint(0, 1000)
    array.append(number)

for j in array:
    if j % 2 == 0 and j % 3 == 0 and j < minim:
        minim = j
print(minim)







