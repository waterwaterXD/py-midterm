from sympy import true


a2 = int(input("請輸入度數:"))
if a2 <=120:
    print("Summer Months",a2*2.10)
    print("No Summer Months",a2*2.10)

elif a2>=121 and a2<=330:
    print("Summer Months",120*2.10+(a2-120)*3.02)
    print("No Summer Months",120*2.10+(a2-120)*2.68)

elif a2>=331 and a2<=500:
    print("Summer Months",120*2.10+(330-120)*3.02+(a2-330)*4.39)
    print("No Summer Months",120*2.10+(330-120)*2.68+(a2-330)*3.61)

elif a2>=501 and a2<=700:
    print("Summer Months",120*2.10+(330-120)*3.02+(500-330)*4.39+(a2-500)*4.97)
    print("No Summer Months",120*2.10+(330-120)*2.68+(500-330)*3.61+(a2-500)*4.01)

elif a2>=701:
    print("Summer Months",120*2.10+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a2-701)*5.63)
    print("No Summer Months",120*2.10+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(a2-701)*4.50)