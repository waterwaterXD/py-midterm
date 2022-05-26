


list1=[["123","456"],["456","789"],["789","888"],["336","558"],["775","666"],["566","221"]]

a=[]
n =int(input("請輸入查詢組數N為："))
for i in range(n):
    a.append(input("第%s組為:" %(i+1)).split(" "))
    #print(a)
    if a[0][0]=="123":
        if a[0][1]=="456":
            print("9000")
        else:
            print("error")
    elif a[0][0]=="456":
        if a[0][1]=="789":
            print("5000")
        else:
            print("error")
    elif a[0][0]=="789":
        if a[0][1]=="888":
            print("6000")
        else:
            print("error")
    elif a[0][0]=="336":
        if a[0][1]=="558":
            print("10000")
        else:
            print("error")
    elif a[0][0]=="775":
        if a[0][1]=="666":
            print("12000")
        else:
            print("error")
    elif a[0][0]=="566":
        if a[0][1]=="221":
            print("7000")
        else:
            print("error")
    else:
        print("error")
            
    a.clear()



