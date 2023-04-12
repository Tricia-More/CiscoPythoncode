#python program to calculate average weight of students on a loop
weight = []
names = []
sum = 0
n = 3
for x in range (n):
    w = float(input('input weight'))
    nam =input('input name')
    weight.append(w)
    names.append(nam)
for i in weight:
    sum += i
for y in names:
    print(y,':', i)
avg = sum/n
print(avg)
for y in range(len(weight)):
    print(weight[y],':',names[y])




