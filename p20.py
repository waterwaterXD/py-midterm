co = int(input("組數為:"))
a =[] #票數放置
sum =0
b = [] #價錢放置
for i in range(co):
    a.append(input("第%s組為:" %(i+1)).split(" "))
    print(a)
for j in range(co):
    sum =int(a[j][0])*250+int(a[j][1])*175
    b.append(sum)
for k in range(len(b)):
    print("第%s組應收費用為：%s" %(k+1,b[k]))




