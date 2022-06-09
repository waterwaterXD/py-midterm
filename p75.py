x=[]
while True:
    y=str(input("請輸入事項(若已無事項,請輸入end):"))
    if y=="end":
        break
    else:
        x.append(y)
for i in range(len(x)):
    print(str(i+1)+".",x[i])