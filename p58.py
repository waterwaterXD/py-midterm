list1=[]
for i in range(10):
    a=input("請輸入第%s個數字:"%(i+1))
    list1.append(a)
list1.sort()#由小到大
print("最大的3個數字為:",list1[-1],",",list1[-2],",",list1[-3])
print("最小的3個數字為:",list1[0],",",list1[1],",",list1[2])