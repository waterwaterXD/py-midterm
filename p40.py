n=int(input(""))
#上
for i in range(1,n,2):  
    print(" "*(n//2)+str(i))

#中左
for j in range(1,n+1,2):
    print(str(j),end="")

#中右
for k in range(n-2,0,-2):
    print(str(k),end="")
print()

#下
for z in range(n-2,0,-2):
    print(" "*(n//2)+str(z))