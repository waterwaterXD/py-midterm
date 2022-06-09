


n=int(input("有幾個班級"))
list1=[]
for i in range(n):
    x=int(input(" "))
    list1.append(x)

print("共需要買",max(list1),"台電腦")