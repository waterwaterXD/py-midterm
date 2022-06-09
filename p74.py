

ans=["red","blue","red","green"]
n=0
a1=a2=a3=a4=0
while n<=10:
    que=input("依序輸入四個顏色(中間以空白間隔)").split(" ")
    n+=1
    if n==10 and que!=ans:
        print("挑戰失敗")
        break
    if que==ans:
        print("正確答案")
        break
    else:
        if (que[0]==ans[0]):
            a1=1
        elif(que[0] in ans):
            a1=2
        else:
            a1=3

        if (que[1]==ans[1]):
            a2=1
        elif(que[1] in ans):
            a2=2
        else:
            a2=3

        if (que[2]==ans[2]):
            a3=1
        elif(que[2] in ans):
            a3=2
        else:
            a3=3
        
        if (que[3]==ans[3]):
            a4=1
        elif(que[3] in ans):
            a4=2
        else:
            a4=3
    print(a1,a2,a3,a4)