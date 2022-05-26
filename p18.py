



dict1={"1":1,"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}

p = input("請輸入五個撲克牌數字:")
sum = 0
p2=p.split(" ") 
for i in range(5):
    if p2[i]=="A":
        sum +=1
    elif p2[i] == "J":
        sum +=11
    elif p2[i] == "Q":
        sum +=12
    elif p2[i] == "K":
        sum +=13
    else:
        sum += int(p2[i])
print(sum)