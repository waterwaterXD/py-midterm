
import random as r

from sympy import cot, true  

while true:
    a1=int(input("輸入第一行正整數為:"))
    a2= input("輸入第二行中數列中的數字為:(空白鍵為分隔)")
    list2=a2.split(" ")
    if len(list2)> a1:
        print("超過了")
        continue
    elif len(list2)<=a1:
        for i in range(0,a1):
            if list2.count(i)==1:
                print("每個數字剛好只出現1次")
                break
            elif list2.count(i)==2:
                print("最大出現次數的數字為:",max(list2))
                print("出現次數為:",list2.count(a1))
                break
    


