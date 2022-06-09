n = int(input("請輸入一個正整數(<=10):"))
if n > 10:
    print("錯誤!")
else:
    for i in range(n): #外部迴圈 (直的)
        for j in range(0,i+1):#內部迴圈(橫的)
            print(str((i+1)*(j+1)) + " ",end="")
        print()