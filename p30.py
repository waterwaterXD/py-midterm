from sqlalchemy import true
a=input("請輸入數字")
b= []
while(true):
    c =input("請輸入數字")
    if c =="0000":
        break
    else:
        b.append(c)
        for i in range(1):#外圍
            d=0
            e=0
            for j in range(4):
                if b[i][j]==a[j]:
                    d +=1
                elif b[i][j] in a:
                    e+=1
        b.clear()
        print(d,"A",e,"B")
    
 
    

    

