
import math   
#math.ceil 無條件進位 
km=float(input("請輸入路程公里數(km):"))
km1=km*1000

km2=km1-1500
if km1<=1500:
    print("所需車資為:75元")
elif km1>1500:
    if (km2)<=250:
        print("所需車資為:",75+5)
    elif (km2)>250:
        print("所需車資為:",75+(math.ceil(km2/250)*5))