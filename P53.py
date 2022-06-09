n=int(input("輸入n值:"))
dict1={}

for i in range(n):
    x=input("請輸入姓名:")#key
    y=input("請輸入電子郵件:")#value
    dict1[x]=y
que=input("請輸入要查詢電子郵件的姓名:")
if que in dict1:
    print(que,"電子郵件帳號為:",dict1[que])
else:
    print("no")