#6

from pickle import TRUE
while(TRUE):
    list6=input("請輸入1~7個數字字串:(以逗號分隔)")
    p6=list (list6.split(","))
    p6.sort()
    p7=sorted(p6,reverse=True)
    if len(p6)>7:
        print("值超過了")
        continue   
    elif len(p6)==7:
        minp6=int(p6[0])*1000000+int(p6[1])*100000+int(p6[2])*10000+int(p6[3])*1000+int(p6[4])*100+int(p6[5])*10+int(p6[6])*10
        maxp6=int(p7[0])*1000000+int(p7[1])*100000+int(p7[2])*10000+int(p7[3])*1000+int(p7[4])*100+int(p7[5])*10+int(p7[6])*10
        
    elif len(p6)==6:
        minp6=int(p6[0])*100000+int(p6[1])*10000+int(p6[2])*1000+int(p6[3])*100+int(p6[4])*10+int(p6[5])*1
        maxp6=int(p7[0])*100000+int(p7[1])*10000+int(p7[2])*1000+int(p7[3])*100+int(p7[4])*10+int(p7[5])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
    elif len(p6)==5:
        minp6=int(p6[0])*10000+int(p6[1])*1000+int(p6[2])*100+int(p6[3])*10+int(p6[4])*1
        maxp6=int(p7[0])*10000+int(p7[1])*1000+int(p7[2])*100+int(p7[3])*10+int(p7[4])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
    elif len(p6)==4:
        minp6=int(p6[0])*1000+int(p6[1])*100+int(p6[2])*10+int(p6[3])*1
        maxp6=int(p7[0])*1000+int(p7[1])*100+int(p7[2])*10+int(p7[3])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
    elif len(p6)==3:
        minp6=int(p6[0])*100+int(p6[1])*10+int(p6[2])*1
        maxp6=int(p7[0])*100+int(p7[1])*10+int(p7[2])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
    elif len(p6)==2: 
        minp6=int(p6[0])*10+int(p6[1])*1
        maxp6=int(p7[0])*10+int(p7[1])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
    elif len(p6)==1: 
        minp6=int(p6[0])*1
        maxp6=int(p7[0])*1
        print("最大值數列與最小值數列差值為:",maxp6-minp6)
        break
        

    