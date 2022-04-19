from random import randrange
from re import A, I


def transpose(list1):
    return [list(row) for row in zip(*list1)]
a1= input("輸入n及m:")
a1.split(" ")
n = a1[0]
m = a1[1]
list1=[]
for i in range(int(n)):
    r = list(input("輸入矩陣數值列:"))
    list1.append(r)
for j in range(0,int(m)):
    list2 = transpose(list1)
    print("輸出矩陣數值第",j+1,"列為:",list2[j])
