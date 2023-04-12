name = []
age = []
sum = 0
n = 2
for x in range (n):
    nam = str(input('Input name:'))
    ag = int(input('Input age:'))
    name.append(nam)
    age.append(ag)
for q in age:
    sum += q
    print('sum=',sum)
for z in name:
    print(z,'is',q,'years old')
avg = sum/n
print('the average age =',avg)

