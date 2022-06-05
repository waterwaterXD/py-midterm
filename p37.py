n = int(input("整數:"))
list1=[]
while (n>0 and n<1000000):
    list1.append(n)
    if n == 1:
        break
    elif n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n / 2
for i in range(len(list1)):
    print(int(list1[i]),end=" ")