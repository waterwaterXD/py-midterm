#7

import math

list7=input("輸入月租費形式及通話時間為:(逗號分隔)")
p7=list7.split(",")
if int(p7[0])==186:
    if int(p7[1])*0.09>186 and int(p7[1])*0.09<372:
        print("通話費為:",math.ceil(int(p7[1])*0.09*0.9))
    elif int(p7[1])*0.09>=372:
        print("通話費為:",math.ceil(int(p7[1])*0.09*0.8))
    elif int(p7[1])*0.09<186:
        print("通話費為:",math.ceil(int(p7[1])*0.09))

elif int(p7[0])==386:
    if int(p7[1])*0.08>186 and int(p7[1])*0.08<772:
        print("通話費為:",math.ceil(int(p7[1])*0.08*0.8))
    elif int(p7[1])*0.08>=772:
        print("通話費為:",math.ceil(int(p7[1])*0.08*0.7))
    elif int(p7[1])*0.08<186:
        print("通話費為:",math.ceil(int(p7[1])*0.08))

elif int(p7[0])==586:   
    if int(p7[1])*0.07>186 and int(p7[1])*0.07<1172:
        print("通話費為:",math.ceil(int(p7[1])*0.07*0.7))
    elif int(p7[1])*0.07>=1172:
        print("通話費為:",math.ceil(int(p7[1])*0.07*0.6))
    elif int(p7[1])*0.08<186:
        print("通話費為:",math.ceil(int(p7[1])*0.07))
