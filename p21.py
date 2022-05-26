a=[["Tom","DTGD"],["Cat","CSIE"],["Nana","ASIE"],["Lim","DBA"],["Won","FDD"]] #二維陣列
a1=input("輸入查詢學號為:")
if a1 == "123":
    print("123",a[0][0],a[0][1])
elif a1 == "456":
    print("456",a[1][0],a[1][1])
elif a1 == "789":
    print("789",a[2][0],a[2][1])
elif a1 == "321":
    print("321",a[3][0],a[3][1])
elif a1 == "654":
    print("654",a[4][0],a[4][1])
else:
    print("沒有這個人")
