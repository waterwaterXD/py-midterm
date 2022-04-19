
s1=str(input("請輸入s1為:"))
s2 =str(input("請輸入s2為:"))
list1=list(s1)
list2=list(s2)
if len(list1)<= len(list2):
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            print("yes")
            break
        else:
            print("no")
            break
else:
    print("no")

