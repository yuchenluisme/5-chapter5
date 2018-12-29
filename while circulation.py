#print number from 1 to 100
x=1
while x<=100:
    print(x)
    x+=1

#for
for number in range(1,11):print(number)

#
d={'x':1,'y':3}
for key in d:print(key,'corresponds to',d[key])
x corresponds to 1
y corresponds to 3

#
names = ['amma', 'betty', 'carol']
ages = [12, 34, 25]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years')

amma is 12
years
betty is 34
years
carol is 25
years

#break结束循环

#
[x*x for x in range(10) if x%3==0]
[0, 9, 36, 81]

#还没写完的程序可以用pass 占位
