a=input("甲方的數字:")
b=input("乙方的數字:")
c=""
for i in range(len(a)):
   if a[i]!=b[i]:
        if a[i]=="1":
            if b[i]=="5":
                c+="贏"
            elif b[i]=="2":
                c+="輸"
            else:
                c+="和"
                
        elif a[i]=="2":
            if b[i]=="1":
                c+="贏"
            elif b[i]=="3":
                c+="輸"
            else:
                c+="和"

        elif a[i]=="3":
            if b[i]=="2":
                c+="贏"
            elif b[i]=="4":
                c+="輸"
            else:
                c+="和"

        elif a[i]=="4":
            if b[i]=="3":
                c+="贏"
            elif b[i]=="5":
                c+="輸"
            else:
                c+="和"
                
        elif a[i]=="5":
            if b[i]=="4":
                c+="贏"
            elif b[i]=="1":
                c+="輸"
            else:
               c+="和"
   else:
       c+="和"
print("洗刷刷結果:",c)