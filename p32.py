from random import randrange


a=input("小明身上有幾元:")
b=input("販賣機有幾種飲料:")
drinks=[]
sum = 0
for i in range(int(b)):
    drinks.append(input(""))
for j in range(int(b)):
    if int(a)>=int(drinks[j]):
        sum+=1
print(sum)