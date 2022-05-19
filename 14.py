from random import uniform
array = []
N = 40
minimum = 0
for i in range(N):
    number = uniform(-100, 100)
    array.append(number)

for i in array:
    if i == array[0]:
        minimum = i
    if i > 0 and i < minimum:
        minimum = i

if minimum == 0:
    print('Положительных элементов нет')
else:
    print(minimum)


print(array)




