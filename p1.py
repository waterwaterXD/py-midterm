#1

p1=int(input("請輸入正整數:"))
list1=[]

for i in range(2,p1):
    if p1%i ==0:
        print("No Prime Found")
        break
    elif i ==p1-1:
        list1.append(i+1)

print(list1)
        