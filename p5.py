#5

M = int(input("請輸入階乘值M:"))
a = 1
total = 1
while(True):    
    if total<=M:
        total *=a
        a+=1
    elif total>=M:
        print("超過M為",M,"的最小階乘值為",a-1)
        break