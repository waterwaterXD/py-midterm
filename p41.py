from webbrowser import Elinks
from wsgiref.validate import InputWrapper


n=int(input("搭了幾次電梯:"))
list1=[]
sum=0
floor=1
while(n >=1 and n<=10):
    for i in range(n):
        a=int(input(" "))
        list1.append(a)
    #print(list1)
    for i in range(len(list1)):
        if list1[i]>floor:
            sum+=20*(list1[i]-floor)  
        elif list1[i]<floor:
            sum+=10*(floor-list1[i])
        floor=list1[i]
    print(sum,"元")