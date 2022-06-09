a=set(input("請輸入string_a:"))
b=set(input("請輸入string_b:"))
c=[]
if(a &b):
    for xx in a:
        if xx in b:
            c.append(xx)
    c.sort()
else:
    print("N")
#print(c)

for i in c:
    print(i,end="")
