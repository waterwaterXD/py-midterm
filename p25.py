


n =input("請輸入考試次數及學生人數:").split(" ")
#print(n)
total=0
b=input("每次考試所佔的比例").split(" ")
a=[]
for i in range(int(n[1])):
    a.append((input("").split(" ")))

for j in range(int(n[1])):
    for k in range(int(n[0])):
        total+=(int(a[j][k]))*float(b[k])
total1=total/int(n[1])
print("全班的總平均值為:%.2f" %(total1))


#sum =int(a[0][0])*0.1 + int(a[0][1])*0.1+int(a[0][2])*0.3+int(a[0][3])*0.1+int(a[0][4])*0.1+int(a[0][5])*0.3
#sum1=int(a[1][0])*0.1 + int(a[1][1])*0.1 +int(a[1][2])*0.3 +int(a[1][3])*0.1 +int(a[1][4])*0.1 +int(a[1][5])*0.3
#sum2=int(a[2][0])*0.1 + int(a[2][1])*0.1 +int(a[2][2])*0.3 +int(a[2][3])*0.1  +int(a[2][4])*0.1  +int(a[2][5])*0.3 
#total =sum+sum1+sum2

#print("全班總平均為%.2f" %(total/3))
