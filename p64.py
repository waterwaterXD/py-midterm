x=int(input("請輸入第一個要判斷的數字:"))
y=int(input("請輸入第二個要判斷的數字:"))
if y==x+2 or x==y+2:
    if x%2!=0 and y%2!=0:
        print("Y")
    else:
        print("N")
else:
    print("N")

