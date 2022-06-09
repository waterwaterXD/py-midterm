n=input("請輸入英文句子:").split(" ")
list1=[]
for i in range(len(n)):
    list1.append(n[i])
list1.reverse()
print("輸出結果:",list1)