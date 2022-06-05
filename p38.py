n=int(input(""))
while(n>=2 and n<=10):
    list1=[]
    for i in range(n):
        a=int(input(""))
        list1.append(a)
#print(list1)
    if a<1 or a>1000:
        break
    else:
        for j in range(len(list1)):
            if list1[j]%9==0 or list1[j]%11==0:
                print("第",j+1,"個點",list1[j])