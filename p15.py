a = list(input("輸入一組四位數字為:"))
a[0]=(int(a[0])+7)%10
a[1]=(int(a[1])+7)%10
a[2]=(int(a[2])+7)%10
a[3]=(int(a[3])+7)%10

a[0],a[2] =a[2],a[0]
a[1],a[3] =a[3],a[1]

print("輸出加密後的數字為:",a[0],a[1],a[2],a[3])

