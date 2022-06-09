
q1=input("請選擇主餐及升級的套餐:")
drink=input("是否升級成大杯飲料:")
frenchfire=input("是否換成大薯:")
total =0
if q1[0]=="1":
    if q1[1]=="A":
        total+=72+55
    elif q1[1]=="B":
        total+=72+68
elif q1[0]=="2":
    if q1[1]=="A":
        total+=62+55
    elif q1[1]=="B":
        total+=62+68
elif q1[0]=="3":
    if q1[1]=="A":
        total+=82+55
    elif q1[1]=="B":
        total+=82+68
elif q1[0]=="4":
    if q1[1]=="A":
        total+=44+55
    elif q1[1]=="B":
        total+=44+68
elif q1[0]=="5":
    if q1[1]=="A":
        total+=60+55
    elif q1[1]=="B":
        total+=60+68
if drink=="是":
    total+=7
if frenchfire=="是":
    total+=13
print("總共為",total,"元")
#print(q1[0])