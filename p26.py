
from sqlalchemy import true



a=input("請輸入要檢測的字串:(end結束)")
while (true):
    if a=="end":
        print("檢測結束")
        break
    else:
        b =input("檢測的字串")
        print("字元",b,"出現次數為",a.count(b))
        a=input("請輸入要檢測的字串:(end結束)")
    